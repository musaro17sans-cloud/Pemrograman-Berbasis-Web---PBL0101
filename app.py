from datetime import datetime
from sanic import Sanic, text

app = Sanic("TugasPBW")


@app.get("/")
async def hello_world(request):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    output = (
        "HELLO WORLD\n\n"
        "#PBW3B1PBL0101\n"
        "251080200117 ABDILLAH LUTFI A\n"
        "Framework Pilihan -> Python [18] - Sanic\n\n"
        f"TIME : {current_time}"
    )
    return text(output)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)