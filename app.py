from flask import Flask, render_template, request

@app.route('/', methods=['GET', 'POST'])
def main():
    

if __name__ == '__main__':
    app.run(port=5000)