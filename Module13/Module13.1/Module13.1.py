from flask import Flask, Response, json

app = Flask(__name__)


@app.route('/primenumber/<number>')
def isPrime(number):
    try:
        num1 = int(number)
        flag = False
        isPrimeNumber = False

        if num1 == 1:
            print(num1, "is not a prime number")
            isPrimeNumber = False
        elif num1 > 1:
            for i in range(2, num1):
                print("FOR number: ", num1)
                if (num1 % i) == 0:
                    flag = True
                    break

            if flag:
                print(num1, "is not a prime number")
                isPrimeNumber = False
            else:
                print(num1, "is a prime number")
                isPrimeNumber = True

        response = {
            "number": num1,
            "isprime": isPrimeNumber,
            "status": 200
        }
        return response

    except ValueError:
        response = {
            "message": "Invalid number added",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response


@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
