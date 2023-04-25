from flask import Flask, render_template, request, session
from mymodules.mai import *

app = Flask(__name__)
app.secret_key = 'my_secret_key'


@app.route('/')
def index():
    context = {
        'title': 'Головна'
    }
    return render_template('index.html', **context)


@app.route('/names', methods=['GET', 'POST'])
def names():
    num_alternatives = int(request.args.get('num_alternatives'))
    num_criteria = int(request.args.get('num_criteria'))

    # Збереження змінної у сесії
    session['num_criteria'] = num_criteria
    session['num_alternatives'] = num_alternatives

    context = {
        'title': 'Імена',
        'num_alternatives': num_alternatives,
        'num_criteria': num_criteria,
    }

    return render_template('names.html', **context)


@app.route('/matrix-krit', methods=['GET', 'POST'])
def matrix_krit():
    num_alternatives = int(session.get('num_alternatives'))
    num_criteria = int(session.get('num_criteria'))

    name_alternatives = request.form.getlist('name_alternatives')
    # Додаємо імена критеріїв до списку
    name_criteria = request.form.getlist('name_criteria')

    # Збереження змінних у сесії
    session['name_alternatives'] = name_alternatives
    session['name_criteria'] = name_criteria

    context = {
        'title': 'Матриця',
        'num_alternatives': num_alternatives,
        'num_criteria': num_criteria,
        'name_alternatives': name_alternatives,
        'name_criteria': name_criteria
    }

    return render_template('matrix_krit.html', **context)


@app.route('/matrix-alt', methods=['GET', 'POST'])
def matrix_alt():
    num_alternatives = int(session.get('num_alternatives'))
    num_criteria = session.get('num_criteria')
    name_alternatives = session.get('name_alternatives')
    name_criteria = session.get('name_criteria')
    matr_krit = request.form.getlist('matrix_krit')

    # Створення списку з матриць по рівнях
    matrix_krit = do_matrix(krit=1, matrix=matr_krit, criteria=num_criteria)

    # Оцінки компонент власного вектора
    components_eigenvector = do_comp_vector(krit=1, criteria=num_criteria, matr=matrix_krit)

    # Нормалізовані оцінки вектора пріоритету
    normalized_eigenvector = do_norm_vector(krit=1, comp_vector=components_eigenvector, criteria=num_criteria)

    # Сума по стовпцям
    sum_col = do_sum_col(krit=1, matr=matrix_krit, criteria=num_criteria)

    # Добуток додатку по стовпцях і нормалізованої оцінки вектора пріоритету
    prod_col = do_prod_col(krit=1, criteria=num_criteria, sum_col=sum_col, norm_vector=normalized_eigenvector)

    # Разом (Lmax)
    l_max = do_l_max(krit=1, prod_col=prod_col, criteria=num_criteria)

    # Індекс узгодженості i Відношення узгодженості
    index_consistency, relation_consistency = do_consistency(krit=1, l_max=l_max, criteria=num_criteria)

    # список для Нормалізованих оцінок вектора пріоритету (для висновку)
    lst_normalized_eigenvector = do_lst_norm_vector(krit=1, name=name_criteria, criteria=num_criteria,
                                                    norm_vector=normalized_eigenvector)

    # Ранжування
    ranj = do_ranj(krit=1, lst_norm_vector=lst_normalized_eigenvector, criteria=num_criteria)

    # Збереження змінних у сесії
    session['matrix_krit'] = matrix_krit
    session['components_eigenvector'] = components_eigenvector
    session['normalized_eigenvector'] = normalized_eigenvector
    session['sum_col'] = sum_col
    session['prod_col'] = prod_col
    session['l_max'] = l_max
    session['index_consistency'] = index_consistency
    session['relation_consistency'] = relation_consistency
    session['lst_normalized_eigenvector'] = lst_normalized_eigenvector
    session['ranj'] = ranj

    context = {
        'title': 'Матриця',
        'num_alternatives': num_alternatives,
        'num_criteria': num_criteria,
        'name_alternatives': name_alternatives,
        'name_criteria': name_criteria,
        'matrix_krit': matrix_krit,
        'components_eigenvector': components_eigenvector,
        'normalized_eigenvector': normalized_eigenvector,
        'sum_col': sum_col,
        'prod_col': prod_col,
        'l_max': l_max,
        'index_consistency': index_consistency,
        'relation_consistency': relation_consistency,
        'lst_normalized_eigenvector': lst_normalized_eigenvector,
        'ranj': ranj,
    }

    # Перевірка відношення узгодженості
    for i in range(len(relation_consistency)):
        if relation_consistency[i] > 15:
            error = f'Перегляньте свої судження у матриці Критерію {name_criteria[i]}'
            context['error'] = error
            break

    return render_template('matrix_alt.html', **context)


@app.route('/result', methods=['GET', 'POST'])
def result():
    num_levels = int(session.get('num_levels'))
    num_alternatives = int(session.get('num_alternatives'))
    num_criteria = session.get('num_criteria')
    name_alternatives = session.get('name_alternatives')
    name_criteria = session.get('name_criteria')
    matrix_krit = session.get('matrix_krit')
    components_eigenvector = session.get('components_eigenvector')
    normalized_eigenvector = session.get('normalized_eigenvector')
    sum_col = session.get('sum_col')
    prod_col = session.get('prod_col')
    l_max = session.get('l_max')
    index_consistency = session.get('index_consistency')
    relation_consistency = session.get('relation_consistency')
    lst_normalized_eigenvector = session.get('lst_normalized_eigenvector')
    ranj = session.get('ranj')
    matr_alt = request.form.getlist('matrix_alt')

    # Створення списку з матриць по рівнях
    matrix_alt = do_matrix(num_alt=num_alternatives, matrix=matr_alt, criteria=num_criteria)

    # Оцінки компонент власного вектора
    components_eigenvector_alt = do_comp_vector(num_alt=num_alternatives, criteria=num_criteria, matr=matrix_alt)

    # Нормалізовані оцінки вектора пріоритету
    normalized_eigenvector_alt = do_norm_vector(num_alt=num_alternatives, comp_vector=components_eigenvector_alt,
                                                criteria=num_criteria)

    # Сума по стовпцям
    sum_col_alt = do_sum_col(num_alt=num_alternatives, matr=matrix_alt, criteria=num_criteria)

    # Добуток додатку по стовпцях і нормалізованої оцінки вектора пріоритету
    prod_col_alt = do_prod_col(num_alt=num_alternatives, criteria=num_criteria, sum_col=sum_col_alt,
                               norm_vector=normalized_eigenvector_alt)

    # Разом (Lmax)
    l_max_alt = do_l_max(prod_col=prod_col_alt, criteria=num_criteria)

    # Індекс узгодженості i Відношення узгодженості
    index_consistency_alt, relation_consistency_alt = do_consistency(num_alt=num_alternatives, l_max=l_max_alt,
                                                                     criteria=num_criteria)

    # список для Нормалізованих оцінок вектора пріоритету (для висновку)
    lst_normalized_eigenvector_alt = do_lst_norm_vector(num_alt=num_alternatives, name=name_alternatives,
                                                        criteria=num_criteria,
                                                        norm_vector=normalized_eigenvector_alt)

    # Ранжування
    ranj_alt = do_ranj(lst_norm_vector=lst_normalized_eigenvector_alt, criteria=num_criteria)

    # Глобальні пріоритети
    global_prior = do_global_prior(norm_vector=normalized_eigenvector,
                                   norm_vector_alt=normalized_eigenvector_alt,
                                   num_alt=num_alternatives)

    # Ранжування глобальних пріоритетів

    lst_normalized_eigenvector_global = do_lst_norm_vector(num_alt=num_alternatives, name=name_alternatives,
                                                           criteria=num_criteria,
                                                           norm_vector=global_prior, g=1)
    ranj_global = do_ranj(lst_norm_vector=lst_normalized_eigenvector_global, criteria=num_criteria, g=1)

    context = {
        'title': 'Результат',
        'num_levels': num_levels,
        'num_alternatives': num_alternatives,
        'num_criteria': num_criteria,
        'name_alternatives': name_alternatives,
        'name_criteria': name_criteria,
        'matrix_krit': matrix_krit,
        'components_eigenvector': components_eigenvector,
        'normalized_eigenvector': normalized_eigenvector,
        'sum_col': sum_col,
        'prod_col': prod_col,
        'l_max': l_max,
        'index_consistency': index_consistency,
        'relation_consistency': relation_consistency,
        'lst_normalized_eigenvector': lst_normalized_eigenvector,
        'ranj': ranj,
        'matrix_alt': matrix_alt,
        'components_eigenvector_alt': components_eigenvector_alt,
        'normalized_eigenvector_alt': normalized_eigenvector_alt,
        'sum_col_alt': sum_col_alt,
        'prod_col_alt': prod_col_alt,
        'l_max_alt': l_max_alt,
        'index_consistency_alt': index_consistency_alt,
        'relation_consistency_alt': relation_consistency_alt,
        'lst_normalized_eigenvector_alt': lst_normalized_eigenvector_alt,
        'ranj_alt': ranj_alt,
        'global_prior': global_prior,
        'lst_normalized_eigenvector_global': lst_normalized_eigenvector_global,
        'ranj_global': ranj_global,
    }

    # Перевірка відношення узгодженості
    for c in range(num_criteria):
        if relation_consistency_alt[c][0] > 15:
            error = f'Перегляньте свої судження у матриці Критерію "{name_criteria[c]}"'
            context['error'] = error

    return render_template('result.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
