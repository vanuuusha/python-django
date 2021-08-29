def correct(text):
    bad_words = ['Это', 'слово', 'нельзя', 'использовать']
    for word in bad_words:
        if word in text:
            return False
    return True


if __name__ == '__main__':
    correct('Это большой текст')
