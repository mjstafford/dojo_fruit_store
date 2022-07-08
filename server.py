from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    straw_count = request.form["strawberry"]
    rasp_count = request.form["raspberry"]
    apple_count = request.form["apple"]
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    student_id = request.form["student_id"]

    print(f"charging {first_name} {last_name} for {int(straw_count) + int(rasp_count) + int(apple_count)} fruits")
    return render_template("checkout.html", strawberry_count = straw_count, raspberry_count = rasp_count, apple_count = apple_count, first_name = first_name, last_name = last_name, student_id=student_id)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html", fruits_list = ["apple", "blackberry", "raspberry", "strawberry"])

if __name__=="__main__":   
    app.run(debug=True)    