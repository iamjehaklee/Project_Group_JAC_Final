from calculations import one_rep_max, week1, week2, week3, week4, open_file
from flask import Flask, render_template, request, redirect, url_for
import pickle, os, os.path

app = Flask(__name__)

app.config['DEBUG'] = True

#post getting user input // get it will render the html 

@app.route('/', methods=['GET', 'POST'])
def create_file():
    """
    This function will first see if a pickle file already exists. If it does, then it will load the user 
    to the workout overview page. If it does not however, it will ask the user to input their 
    weights and reps. Once that happens, it will save their max weights as a dictionary into a pickle file and 
    redirect the user to the workout overview page. 
    """
    filename = 'user_lift'
    if not os.path.exists(filename+'.pickle'):
        if request.method == 'POST':
            #Input weights from user 
            bench_weight = int(request.form['weight1']) #fill in
            bench_reps = int(request.form['reps1']) #fill in
            military_weight = int(request.form['weight2']) #fill in
            military_reps = int(request.form['reps2']) #fill in
            squat_weight = int(request.form['weight3']) #fill in
            squat_reps = int(request.form['reps3']) #fill in
            deadlift_weight = int(request.form['weight4']) #fill in 
            deadlift_reps = int(request.form['reps4'])   #fill in 

            #Outputs max for user 
            bench_max_weight = one_rep_max(bench_weight, bench_reps)  
            military_max_weight = one_rep_max(military_weight, military_reps)
            squat_max_weight = one_rep_max(squat_weight, squat_reps)
            deadlift_max_weight = one_rep_max(deadlift_weight, deadlift_reps)

            total_max_lifts = {} 

            total_max_lifts['bench'] = bench_max_weight
            total_max_lifts['military'] = military_max_weight
            total_max_lifts['squat'] = squat_max_weight
            total_max_lifts['deadlift'] = deadlift_max_weight
            filename += '.pickle'
            # if os.path.exists(filename):
            f = open(filename,'wb')
            pickle.dump(total_max_lifts,f)     
            f.close()
            return render_template('workouts.htm')
        return render_template('index.htm') 
    else:
        return render_template('workouts.htm')

"""
All the code below builds out the web links. 
"""

@app.route('/workouts.htm')
def workouts():
    return render_template('workouts.htm')
@app.route('/week1.htm')
def week1():
    return render_template('week1.htm')
@app.route('/week2.htm')
def week2():
    return render_template('week2.htm')
@app.route('/week3.htm')
def week3():
    return render_template('week3.htm')
@app.route('/week4.htm')
def week4():
    return render_template('week4.htm')

from calculations import one_rep_max, week1, week2, week3, week4, open_file

@app.route('/w1day1.htm')
def week1day1():
    max_lifts = open_file('user_lift.pickle')
    military_weight_set1 = round(week1.set_1(max_lifts['military']))
    military_weight_set2 = round(week1.set_2(max_lifts['military']))
    military_weight_set3 = round(week1.set_3(max_lifts['military']))
    bench_weight = round(0.5*max_lifts['bench'])
    return render_template('w1day1.htm', military_weight_set1=military_weight_set1, military_weight_set2=military_weight_set2, military_weight_set3=military_weight_set3, bench_weight = bench_weight)

@app.route('/w1day2.htm')
def week1day2():
    max_lifts = open_file('user_lift.pickle')
    deadlift_set1 = round(week1.set_1(max_lifts['deadlift']))
    deadlift_set2 = round(week1.set_2(max_lifts['deadlift']))
    deadlift_set3 = round(week1.set_3(max_lifts['deadlift']))
    squat_weight = round(0.5*max_lifts['squat'])
    return render_template('w1day2.htm', deadlift_set1=deadlift_set1, deadlift_set2=deadlift_set2, deadlift_set3=deadlift_set3, squat_weight=squat_weight)

@app.route('/w1day3.htm')
def week1day3():
    max_lifts = open_file('user_lift.pickle')
    bench_set1 = round(week1.set_1(max_lifts['bench']))
    bench_set2 = round(week1.set_2(max_lifts['bench']))
    bench_set3 = round(week1.set_3(max_lifts['bench']))
    military_weight = round(0.5*max_lifts['military'])
    return render_template('w1day3.htm', bench_set1=bench_set1, bench_set2=bench_set2, bench_set3=bench_set3, military_weight=military_weight)

@app.route('/w1day4.htm')
def week1day4():
    max_lifts = open_file('user_lift.pickle')
    squat_set1 = round(week1.set_1(max_lifts['squat']))
    squat_set2 = round(week1.set_2(max_lifts['squat']))
    squat_set3 = round(week1.set_3(max_lifts['squat']))
    deadlift_weight = round(0.5*max_lifts['deadlift'])
    return render_template('w1day4.htm', squat_set1=squat_set1, squat_set2=squat_set2, squat_set3=squat_set3, deadlift_weight=deadlift_weight)

@app.route('/w2day1.htm')
def week2day1():
    max_lifts = open_file('user_lift.pickle')
    military_weight_set1 = round(week2.set_1(max_lifts['military']))
    military_weight_set2 = round(week2.set_2(max_lifts['military']))
    military_weight_set3 = round(week2.set_3(max_lifts['military']))
    bench_weight = round(0.5*max_lifts['bench'])
    return render_template('w2day1.htm', military_weight_set1=military_weight_set1, military_weight_set2=military_weight_set2, military_weight_set3=military_weight_set3, bench_weight=bench_weight)

@app.route('/w2day2.htm')
def week2day2():
    max_lifts = open_file('user_lift.pickle')
    deadlift_set1 = round(week2.set_1(max_lifts['deadlift']))
    deadlift_set2 = round(week2.set_2(max_lifts['deadlift']))
    deadlift_set3 = round(week2.set_3(max_lifts['deadlift']))
    squat_weight = round(0.5*max_lifts['squat'])
    return render_template('w2day2.htm', deadlift_set1=deadlift_set1, deadlift_set2=deadlift_set2, deadlift_set3=deadlift_set3, squat_weight=squat_weight)

@app.route('/w2day3.htm')
def week2day3():
    max_lifts = open_file('user_lift.pickle')
    bench_set1 = round(week2.set_1(max_lifts['bench']))
    bench_set2 = round(week2.set_2(max_lifts['bench']))
    bench_set3 = round(week2.set_3(max_lifts['bench']))
    military_weight = round(0.5*max_lifts['military'])
    return render_template('w2day3.htm', bench_set1=bench_set1, bench_set2=bench_set2, bench_set3=bench_set3, military_weight=military_weight)

@app.route('/w2day4.htm')
def week2day4():
    max_lifts = open_file('user_lift.pickle')
    squat_set1 = round(week2.set_1(max_lifts['squat']))
    squat_set2 = round(week2.set_2(max_lifts['squat']))
    squat_set3 = round(week2.set_3(max_lifts['squat']))
    deadlift_weight = round(0.5*max_lifts['deadlift'])
    return render_template('w2day4.htm', squat_set1=squat_set1, squat_set2=squat_set2, squat_set3=squat_set3, deadlift_weight=deadlift_weight)

@app.route('/w3day1.htm')
def week3day1():
    max_lifts = open_file('user_lift.pickle')
    military_weight_set1 = round(week3.set_1(max_lifts['military']))
    military_weight_set2 = round(week3.set_2(max_lifts['military']))
    military_weight_set3 = round(week3.set_3(max_lifts['military']))
    bench_weight = round(0.5*max_lifts['bench'])
    return render_template('w3day1.htm', military_weight_set1=military_weight_set1, military_weight_set2=military_weight_set2, military_weight_set3=military_weight_set3, bench_weight=bench_weight)

@app.route('/w3day2.htm')
def week3day2():
    max_lifts = open_file('user_lift.pickle')
    deadlift_set1 = round(week3.set_1(max_lifts['deadlift']))
    deadlift_set2 = round(week3.set_2(max_lifts['deadlift']))
    deadlift_set3 = round(week3.set_3(max_lifts['deadlift']))
    squat_weight = round(0.5*max_lifts['squat'])
    return render_template('w3day2.htm', deadlift_set1=deadlift_set1, deadlift_set2=deadlift_set2, deadlift_set3=deadlift_set3, squat_weight=squat_weight)

@app.route('/w3day3.htm')
def week3day3():
    max_lifts = open_file('user_lift.pickle')
    bench_set1 = round(week3.set_1(max_lifts['bench']))
    bench_set2 = round(week3.set_2(max_lifts['bench']))
    bench_set3 = round(week3.set_3(max_lifts['bench']))
    military_weight = round(0.5*max_lifts['military'])
    return render_template('w3day3.htm', bench_set1=bench_set1, bench_set2=bench_set2, bench_set3=bench_set3, military_weight=military_weight)

@app.route('/w3day4.htm')
def week3day4():
    max_lifts = open_file('user_lift.pickle')
    squat_set1 = round(week3.set_1(max_lifts['squat']))
    squat_set2 = round(week3.set_2(max_lifts['squat']))
    squat_set3 = round(week3.set_3(max_lifts['squat']))
    deadlift_weight = round(0.5*max_lifts['deadlift'])
    return render_template('w3day4.htm', squat_set1=squat_set1, squat_set2=squat_set2, squat_set3=squat_set3, deadlift_weight=deadlift_weight)

@app.route('/w4day1.htm')
def week4day1():
    max_lifts = open_file('user_lift.pickle')
    military_weight_set1 = round(week4.set_1(max_lifts['military']))
    military_weight_set2 = round(week4.set_2(max_lifts['military']))
    military_weight_set3 = round(week4.set_3(max_lifts['military']))
    bench_weight = round(0.5*max_lifts['bench'])
    return render_template('w4day1.htm', military_weight_set1=military_weight_set1, military_weight_set2=military_weight_set2, military_weight_set3=military_weight_set3, bench_weight=bench_weight)

@app.route('/w4day2.htm')
def week4day2():
    max_lifts = open_file('user_lift.pickle')
    deadlift_set1 = round(week4.set_1(max_lifts['deadlift']))
    deadlift_set2 = round(week4.set_2(max_lifts['deadlift']))
    deadlift_set3 = round(week4.set_3(max_lifts['deadlift']))
    squat_weight = round(0.5*max_lifts['squat'])
    return render_template('w4day2.htm', deadlift_set1=deadlift_set1, deadlift_set2=deadlift_set2, deadlift_set3=deadlift_set3, squat_weight=squat_weight)

@app.route('/w4day3.htm')
def week4day3():
    max_lifts = open_file('user_lift.pickle')
    bench_set1 = round(week4.set_1(max_lifts['bench']))
    bench_set2 = round(week4.set_2(max_lifts['bench']))
    bench_set3 = round(week4.set_3(max_lifts['bench']))
    military_weight = round(0.5*max_lifts['military'])
    return render_template('w4day3.htm', bench_set1=bench_set1, bench_set2=bench_set2, bench_set3=bench_set3, military_weight=military_weight)

@app.route('/w4day4.htm')
def week4day4():
    max_lifts = open_file('user_lift.pickle')
    squat_set1 = round(week4.set_1(max_lifts['squat']))
    squat_set2 = round(week4.set_2(max_lifts['squat']))
    squat_set3 = round(week4.set_3(max_lifts['squat']))
    deadlift_weight = round(0.5*max_lifts['deadlift'])
    return render_template('w4day4.htm', squat_set1=squat_set1, squat_set2=squat_set2, squat_set3=squat_set3, deadlift_weight=deadlift_weight)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

