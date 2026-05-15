
def tag(name, *content, cls=None, **kwargs):
    ''' Генерирует один или несколько HTML-тегов '''
    if cls is not None:
        kwargs['class'] = cls
    if kwargs:
        kwargs_str = ''.join('%s="%s"' % (attr, value) for attr, value in sorted(kwargs.items()))
    else:
        kwargs_str = ''
    if content:
        return '\n'.join('<%s %s>%s</%s>' % (name, kwargs_str, c, name) for c in content)
    else:
        return '<%s %s />' % (name, kwargs_str)


def main():
    print(tag('br')) # <br  />
    print(tag('p', 'hello')) # <p >hello</p>
    print(tag('p', 'hello', 'world', cls='sidebar')) # <p class="sidebar">hello</p>
    print(tag(content='testing', name='img')) # <img content="testing" />


if __name__ == '__main__':
    main()
