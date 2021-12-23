# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 11:04:26 2021

@author: LENOVO
"""
import cv2
import mediapipe as mp
import math

id1=[]
id2=[]
def degree_calculation_of_face(id1,id2):
    m2 = (id2[0][2]-id2[1][2])/(id2[0][1]-id2[1][1])
    m1= (id1[0][2]-id1[1][2])/(id1[0][1]-id1[1][1])
    degree=math.degrees(math.atan((m2-m1)/(1+m2*m1)))
    print(degree)
    if degree<0:
        degree=-degree
        return degree
    else:
        return degree
    
def degree_calculation_of_hand(id1,id2):
    try:
        m2 = (id2[0][2]-id2[1][2])/(id2[0][1]-id2[1][1])
        m1= (id1[0][2]-id1[1][2])/(id1[0][1]-id1[1][1])
        degree=math.degrees(math.atan((m2-m1)/(1+m2*m1)))
    except:
        return 0
    print(degree)
    if degree<0:
        degree=-degree
        return degree
    else:
        return degree
    
def degree_calculation(id1,id2,p1,p2):
    try:
        if id1[p1][0]==p1 and id1[p2][0]==p2:
            try:
                m2 = (id2[1][2]-id2[0][2])/(id2[1][1]-id2[0][1])
                m1= (id1[1][2]-id1[0][2])/(id1[1][1]-id1[0][1])
                degree=math.degrees(math.atan((m2-m1)/(1+m2*m1)))
            except:
                return 0
            if degree<0:
                degree=-degree
            return degree
        else:
            return 0
    except:
        return 0
    
def main(video,option):
    mpPose = mp.solutions.pose
    pose = mpPose.Pose()
    cap = cv2.VideoCapture(video)
    count=0
    max_degree=0
    if option>2 and option<7:
        while True:
            id2=[]
            success, img = cap.read()
            if count==0:                     # exit if Escape is hit
                  if img != []:
                      imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                      results = pose.process(imgRGB)
                        # print(results.pose_landmarks)
                      if results.pose_landmarks:
                            results = pose.process(imgRGB)
                            for id, lm in enumerate(results.pose_landmarks.landmark):
                                if id==10 or id==9:
                                    h, w, c = img.shape
                                    cx, cy= int(lm.x * w), int(lm.y * h)
                                    id1.append([id,cx,cy])
                                    count += 1
            else:
                if img != []:
                    try:
                        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    except :
                        break
                    results = pose.process(imgRGB)
                        # print(results.pose_landmarks)
                    if results.pose_landmarks:
                            results = pose.process(imgRGB)
                            for id, lm in enumerate(results.pose_landmarks.landmark):
                                if id==10 or id==9:
                                    h, w, c = img.shape
                                    cx, cy= int(lm.x * w), int(lm.y * h)
                                    id2.append([id,cx,cy])
                    #print(id2)
                    if degree_calculation_of_face(id1,id2)>max_degree:             
                        max_degree=degree_calculation_of_face(id1,id2)
                    
        return max_degree
    
    elif option>6 and option<17:
            max_degree=-1
            count=0
            while True:
                id2=[]
                success, img = cap.read()
                if count==0:                     # exit if Escape is hit
                      if img != []:
                        try:
                            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        except:
                            break
                        results = pose.process(imgRGB)
                        # print(results.pose_landmarks)
                        if results.pose_landmarks:
                            results = pose.process(imgRGB)
                            for id, lm in enumerate(results.pose_landmarks.landmark):
                                if id==12 or id==14:
                                    h, w, c = img.shape
                                    cx, cy= int(lm.x * w), int(lm.y * h)
                                    if lm.visibility>0.5:
                                        id1.append([id,cx,cy])
                      count+=1
                else:
                    if img != []:
                        try:
                            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        except:
                            break
                        results = pose.process(imgRGB)
                        # print(results.pose_landmarks)
                        if results.pose_landmarks:
                            results = pose.process(imgRGB)
                            for id, lm in enumerate(results.pose_landmarks.landmark):
                                if id==12 or id==14:
                                    h, w, c = img.shape
                                    cx, cy= int(lm.x * w), int(lm.y * h)
                                    if lm.visibility>0.5:
                                        id2.append([id,cx,cy])
                    if degree_calculation(id1,id2)>max_degree:             
                        max_degree=degree_calculation(id1,id2)
            return max_degree
        
    elif option>16 and option<21:   
        mpHands = mp.solutions.hands
        hands = mpHands.Hands()
        max_degree=-1
        count=0
        while True:
            id2=[]
            success, img = cap.read()
            if count==0:                     # exit if Escape is hit
                if img != []:
                        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        results = hands.process(imgRGB)
                        if results.multi_hand_landmarks:
                            for handLms in results.multi_hand_landmarks:
                                for id, lm in enumerate(handLms.landmark):
                                    if id==5 or id==9:
                                        h, w, c = img.shape
                                        cx, cy = int(lm.x * w), int(lm.y * h)
                                        id1.append([id,cx,cy])
                            count+=1
            else:
                    if img != []:
                        try:
                            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                            results = hands.process(imgRGB)
                            if results.multi_hand_landmarks:
                                for handLms in results.multi_hand_landmarks:
                                    for id, lm in enumerate(handLms.landmark):
                                        if id==5 or id==9:
                                            h, w, c = img.shape
                                            cx, cy = int(lm.x * w), int(lm.y * h)
                                            id2.append([id,cx,cy])
                                            
                            if degree_calculation_of_hand(id1,id2)>max_degree:             
                                    max_degree=degree_calculation_of_hand(id1,id2)
                                    print(max_degree)
                        except:
                            break
        return max_degree

video='MotionsNew/Mov17-2.mp4'
print(main(video, 17))
