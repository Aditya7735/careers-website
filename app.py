from flask import Flask, render_template
app = Flask(__name__)
JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        'salary': 'Rs. 12,00,000'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'Bhubaneswar, India',
        'salary': 'Rs. 21,00,000'
    }
]
@app.route('/')
def home():
    return render_template('home.html',jobs=JOBS)

print(__name__)
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)