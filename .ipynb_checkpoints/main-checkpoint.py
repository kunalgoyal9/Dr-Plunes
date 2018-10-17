from collections import defaultdict
import json
from flask import Flask, request, make_response, jsonify
import numpy as np
import pandas as pd
import requests as rq
import random
from random import choice

app = Flask(__name__)
log = app.logger

@app.route('/', methods=["POST"])
def webhook():
    req = request.get_json(silent=True, force=True)
    action = req.get('queryResult').get('action')
    try:
        if action == 'symptoms-pregnancy':
            disease = req["queryResult"]["parameters"]["Disease"]
            if disease == 'lbp':
                string = f"During the pregnancy time Signs and symptoms of low blood pressure such as\n Dizziness, lightheadedness, especially when standing or sitting up, Fainting, Nauseal, Tiredness, Blurred vision, Unusual thirst, Clammy, pale, or cold skin."
            elif disease == 'hbp':
                string = f"During the pregnancy time Signs and symptoms of high blood pressure such as \n Rapid weight gain caused by a significant increase in bodily fluid, Abdominal pain, Severe headaches, Change in reflexes, Reduced urine or no urine output, Dizziness, Excessive vomiting and nausea, Vision changes"

        elif action == 'symptoms':
            disease = req["queryResult"]["parameters"]["Disease"]
            if disease == 'lbp':
                string = f"Low blood pressure signals an underlying problem, especially when it drops suddenly or is accompanied by symptoms such as: Fatigue, Lightheadedness, Dizziness, Nausea, Clammy skin, Depression, Loss of consciousness, Blurry vision"

            elif disease == 'hbp':
                string = f"There are some symptoms of high blood pressure in both of men and women such as: Severe headache, Fatigue or confusion, Vision problems, Chest pain, Difficulty breathing, Irregular heartbeat, Blood in the urine, Pounding in your chest, neck, or ears."

        elif action == 'causes':
            disease = req["queryResult"]["parameters"]["Disease"]
            if disease == 'lbp':
                string = f"Some of the most common causes include: Nutritional deficiencies, Prolonged bed rest, Pregnancy, Medications, Severe infections, Allergic reactions, Fall in blood volume, Heart issues, dehydration, bleeding, inflammation"

            elif disease == 'hbp':
                string = f"The exact causes of high blood pressure are not known, but several things may play a role which is given below: Smoking, Being overweight or obese, Lack of physical activity, Too much salt in the diet, Too much alcohol consumption (more than 1 to 2 drinks per day), Stress, Older age, Genetics, Family history of high blood pressure, Adrenal and thyroid disorders, Sleep apnea"

        elif action == 'causes-food':
            disease = req["queryResult"]["parameters"]["Disease"]
            if disease == 'lbp':
                string = f"If you want know about food that causes low blood pressure then you can instantly hire doctor on plunes.com"

            elif disease == 'hbp':
                string = f"The foods and drinks which is the causes of high blood pressure such as: Salt, Deli meat, Frozen pizza, Pickles, Canned soups, Tomato products, Sugar, Packaged foods, If you want know about solutions then you can directly contact plunes.com"

        elif action == 'treatment':
            disease = req["queryResult"]["parameters"]["Disease"]
            if disease == 'lbp':
                string = f"You can perform deep breaths, inhale and exhale for more than 4 mintues to reduce the blood pressure. For more information you can hire a doctor from Plunes instantly."

            elif disease == 'hbp':
                string = f"Few natural ways to combat high blood pressure. Walk and exercise regularly. Exercise is one of the best things you can do to lower high blood pressure, Reduce your sodium intake, Eat less salt, Drink less alcohol, Eat more potassium-rich foods, Cut back on caffeine, Learn to manage stress, Eat dark chocolate or cocoa, Lose weight.For more info, you can ask doctors on Plunes.com about your any query for curated, and validated solutions."

        elif action == 'treatment-food':
            disease = req["queryResult"]["parameters"]["Disease"]
            if disease == 'lbp':
                string = f"Drinking soda water or lemonade is beneficial to reduce the blood pressure in few minutes. Also sit and take deep breaths. For more information you can hire a doctor from Plunes instantly."

            elif disease == 'hbp':
                string = f"Berries.Especially Blueberries, Red beets, Skim milk and yogurt, Oatmeal, Bananas, Salmon, mackerel, and fish with omega-3s, Seeds. Sunflower, Pumpkin or Squash Seeds. Also foods rich in potassium helps your kidneys get rid of more sodium through your urine. Nonfat Milk. rich in potassium and calcium, good for curing blood pressure. Hibiscus Tea. Cranberry Juice."    

        elif action == 'hbp_lbp_definetion':
            disease = req["queryResult"]["parameters"]["Disease"]
            if disease == 'lbp':
                string = f"Hypotension is the medical term for low blood pressure. It is the condition when blood pressure is less than (90/60mmHg)"

            elif disease == 'hbp':
                string = f"High blood pressure, or hypertension, occurs when your blood pressure increases to unhealthy levels. Your blood pressure measurement takes into account how much blood is passing through your blood vessels and the amount of resistance the blood meets while the heart is pumping. In high Blood pressure, Blood pressure exceed with (120/80mmHg)" 
    except:
        string = 'Oops this is beyond my comprehension level at the moment, you can hire a doctor instantly from Plunes.'
    return make_response(jsonify({'fulfillmentText': string}))
        

if __name__ == '__main__':
    user_sessions = defaultdict()
    app.run(port='4000', debug=True)
