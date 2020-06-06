from flask import Flask, render_template, request, url_for

app = Flask(__name__, static_url_path='/static')

lists = [{'title':'welcome', 'text':'welcome'}]

count = 0

@app.route('/')
def main_get(posts=None):
    global count
    global lists
    return render_template('index.html', posts=lists, count = count)

@app.route('/give')
def give(title = None, text=None, is_blank='true'):
    global count
    global lists


    is_blank = request.args.get('blank')
    title = request.args.get('tit')
    text = request.args.get('text')


    print(f'blank : {is_blank}')

    if (title != None or title != 'None') and is_blank != 'true' and text != None:

        for list in lists:
            if list['title'] == title:
                return render_template('index.html', posts=lists)
        post = {}
        print(f"title : {title}")

        post['title'] = title
        post['text']= text


        lists.append(post)

        count+= 1

    return render_template('index.html', posts=lists, count = count)

@app.route('/get/')
def get():
    global lists
    return render_template('write.html')


@app.route('/show')
def show():
    num = request.args.get('num')
    global lists
    return render_template('show.html', post=lists[int(num)])

if __name__ == '__main__':
    # threaded=True 로 넘기면 multiple plot이 가능해짐
  app.run()
