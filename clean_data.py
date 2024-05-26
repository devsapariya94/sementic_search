import os 

import re 

for file in os.listdir('assignment-summer-intern-2024/samples'):
    if file.endswith('.txt'):
        with open(f'assignment-summer-intern-2024/samples/{file}', 'r') as f:
            text = f.read()
            text = re.sub(r'\n', ' ', text)
            text = re.sub(r'\s+', ' ', text)

            # delete all the things before first occurence of 'customer stories /'
            text = re.sub(r'.*customer stories /', '', text, flags=re.IGNORECASE)
            # delete all the things after first occurence of 'customer stories /'
            text = re.sub(r'We’re proud to be recognized as an industry leader, view our full list of honors to learn more./*', '', text, flags=re.IGNORECASE)
            with open(f'clean_data/{file}', 'w') as f:
                f.write(text)


# renameing files

for file in os.listdir('clean_data'):
    if file.endswith('.txt'):
        # new name will be the text which occurs before the first occurence of : in the file content
        with open(f'clean_data/{file}', 'r') as f:
            text = f.read()
            new_name = text.split(':')[0]
        os.rename(f'clean_data/{file}', f'clean_data/{new_name}.txt')
        print(f'clean_data/{file} renamed to clean_data/{new_name}.txt')

