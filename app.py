from flask import Flask, render_template,redirect

app = Flask(__name__)

domains_arr = [
    {
        "domain_name": "Domain_1",
        "repo_url": "https://github.com/repo1",
        "domain_image": "../static/images/domain_1.png"
    },{
        "domain_name": "Domain_2",
        "repo_url": "https://github.com/repo2",
        "domain_image": "../static/images/domain_2.jpg"
    },{
        "domain_name": "Domain_3",
        "repo_url": "https://github.com/repo3",
        "domain_image": "../static/images/domain_1.png"
    },{
        "domain_name": "Domain_4",
        "repo_url": "https://github.com/repo4",
        "domain_image": "../static/images/domain_1.png"
    },{
        "domain_name": "Domain_5",
        "repo_url": "https://github.com/repo5",
        "domain_image": "../static/images/domain_1.png"
    }
]

@app.route('/')
def index():
    return render_template('index.html', domains=domains_arr)

@app.route('/domain/<string:domain_name>')
def domain_page(domain_name):
    def filter_1(x):
        return x['domain_name'] == domain_name
    print(domain_name)
    result = filter(filter_1, domains_arr)
    result=list(result)
    print(result)
    return render_template('domain_page.html',domain=result[0])

if __name__ == '__main__':
    app.run(debug=True)



