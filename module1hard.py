import statistics

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students) # преобразовали множество в список и расставили в алфавитном порядке
average_score = statistics.mean(grades [0]), statistics.mean(grades [1]), statistics.mean(grades [2]), statistics.mean(grades [3]), statistics.mean(grades [4]) # рассчитали среднее арифметическое для каждого элемента в списке
grade = dict(zip(students, average_score))
print(grade)
