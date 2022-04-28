from flask import Flask,render_template,request

app=Flask(__name__)
@app.route('/')
def home_page():
    return render_template('home_page.html')


@app.route('/display',methods=['GET','POST'])
def display_page():
    name=request.form['use_name']
    return render_template('result.html',my_name=name)


if '__main__'==__name__:
    app.run(debug=True)