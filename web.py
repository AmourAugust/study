from flask import Flask,render_template,request,redirect,url_for,Response
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


def draw_bar(data):
    x = []
    H_score = []
    OTCE = []
    Dice = []
    for lines in data:
        print(lines)
        x.append(lines[0])
        H_score.append(float(lines[1]))
        OTCE.append(float(lines[2]))
        Dice.append(float(lines[3]))
    # print(x)
    # print(Dice)
    result_list = sorted(zip(Dice,x), reverse=True)
    # print(result_list)
    sorted_id = sorted(range(len(Dice)), key = lambda x:Dice[x], reverse=True)
    # print(Dice)
    plt.figure(figsize=(12,8))
    plt.bar(range(len(Dice)), [i for i,_ in result_list], tick_label=[i for _,i in result_list], facecolor="#6600CC")  
    plt.xticks(rotation=60)
    plt.xlabel("source name")#x轴上的名字
    plt.ylabel("Dice")#y轴上的名字
    plt.ylim(0.55,0.75)
    plt.savefig("static/images/demo/bar_plot.png")



mod_ana = [
            ["ED-14-T1", "ED-14-T2", "NCR-14-T1", "NCR-14-T2", ], 
            ["ED-13-T1", "ED-13-T2", "NCR-13-T1", "NCR-13-T2", ], 
            ["ED-17-T1", "ED-17-T2", "NCR-17-T1", "NCR-17-T2",], 
            ["ED-18-T1", "ED-18-T2", "NCR-18-T1", "NCR-18-T2",], 
          ]
roi_ana = [["ED-14-T2", "NCR-14-T2", "ED-13-T2", "NCR-13-T2", ], ["ED-17-T2", "NCR-17-T2", "ED-18-T2", "NCR-18-T2", ], ]
trans_data = [["ED-14-T2", "0.1887", "-0.0226", ], ["ED-13-T2", "1.4031", "-0.0356", ], ["ED-17-T2", "1.3327", "-0.0389", ], ["ED-18-T2", "0.2776", "-0.0273"], ]
final_results = [
    ["ED-14-T1", "-0.0380", "-0.0395", "0.664", ],
    ["ED-14-T2", "0.1887", "-0.0226", "0.703", ],
    ["NCR-14-T1", "0.8990", "-0.0395", "0.646", ],
    ["NCR-14-T2", "0.5140", "-0.0383", "0.660", ],
    ["ED-13-T1", "0.4142", "-0.0407", "0.657", ],
    ["ED-13-T2", "1.4031", "-0.0356", "0.695", ],
    ["NCR-13-T1", "5.0050", "-0.0407", "0.628", ],
    ["NCR-13-T2", "10.5247", "-0.0401", "0.683", ],
    ["ED-17-T1", "0.3525", "-0.0435", "0.697", ],
    ["ED-17-T2", "1.3327", "-0.0389", "0.708", ],
    ["NCR-17-T1", "1.5211", "-0.0436", "0.612", ],
    ["NCR-17-T2", "6.6535", "-0.0433", "0.681", ],
    ["ED-18-T1", "0.1070", "-0.0435", "0.675", ],
    ["ED-18-T2", "0.2776", "-0.0273", "0.707", ],
    ["NCR-18-T1", "0.9038", "-0.0436", "0.664", ],
    ["NCR-18-T2", "2.2038", "-0.0394", "0.666", ],

]

table = {}
table["mod_ana"] = mod_ana
table["roi_ana"] = roi_ana
table["trans_data"] = trans_data
table["final_results"] = final_results
print(table)
# draw_bar(table["final_results"])

app = Flask(__name__)
app.debug=True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/demonstration',methods=["GET", "POST"])
def demonstration():
    if request.method == 'POST':
        print("hh")
        target_name = request.form.get('targetname')
        print(target_name)
        return render_template('1.html',target_name=target_name)
    draw_bar(table["final_results"])
    return render_template('1.html', tables = table)


@app.route('/demonstration/<targetname>')
def demon(target_name):
    return render_template('1.html',target_name=target_name)


@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/plot.png')
def plot_png():
    fig = draw_bar()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    # app.run(host='127.0.0.1',port=5000)
    app.run(host='0.0.0.0',port=15000)

