from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from plezalnikback.models import User, Achievement

# Create your views here.

def login(request):
    return render_to_response('login.html', {})

def index(request):
    return render_to_response('home.html', {})

def style(request):
    user = request.GET.get('user')
    return render_to_response('style.html', {'user':user})

def gradenumber(request):
    user = request.GET.get('user')
    full_name = request.GET.get('full_name')
    fb_id = request.GET.get('fb_id')
    achievement_type = request.GET.get('achievement_type')
    return render_to_response('gradenumber.html', {'user':user, 'style':achievement_type})

def gradeletter(request):
    user = request.GET.get('user')
    achievement_type = request.GET.get('achievement_type')
    grade_no = request.GET.get('grade_no')
    return render_to_response('gradeletter.html', {'user':user, 'style':achievement_type, 'grade_no':grade_no})

def gradefinish(request):
    user = request.GET.get('user')
    achievement_type = request.GET.get('achievement_type')
    grade_no = request.GET.get('grade_no')
    grade_letter = request.GET.get('grade_letter')
    return render_to_response('gradefinish.html', {'user':user, 'style':achievement_type, 'grade_no':grade_no, 'grade_letter':grade_letter})

def speed(request):
    user = request.GET.get('user')
    achievement_type = request.GET.get('achievement_type')
    grade_no = request.GET.get('grade_no')
    grade_letter = request.GET.get('grade_letter')
    return render_to_response('speed.html', {'user':user, 'style':achievement_type, 'grade_no':grade_no, 'grade_letter':grade_letter})

def createachievement(request):
    user = request.GET.get('user')
    achievement_type = request.GET.get('achievement_type')
    grade_no = request.GET.get('grade_no')
    grade_letter = request.GET.get('grade_letter')
    speed = request.GET.get('speed')
    achievement = Achievement(user=user, achievement_type=achievement_type, grade_no=grade_no, grade_letter=grade_letter, speed=speed)
    achievement.save()
    return HttpRequest(1)
    #return render_to_response('speed.html', {'user':user, 'style':achievement_type, 'grade_no':grade_no, 'grade_letter':grade_letter, 'speed':speed})
    
        

def leaderboard(request):
    achievements = Achievement.objects.all().order_by('grade_no').reverse()
    achievement = Achievement(grade_no=request.GET.get('grade_no'), grade_letter=request.GET.get('grade_letter'))
    
    
    #new_achievements = []
    #for achievement in achievements:
    #    achievement.ocena = achievement.ocena()
    #    new_achievements.append(achievement)
    
    #previous = new_achievements[0]
    #i=0
    #a=1
    #b=2
    #c=3
    
    #for achievement in achievements:
    #    if previous.ocena[0] == achievement.ocena[0]:
    #        if previous[1] < achievement[1]:
    #            new_achievements.pop(i)
    #            new_achievements.insert(achievement, i-1)
    #            i+=1
    #            previous = achievement
    
    
    #achievement.save()
    #achievement = achievements[0]
    return render_to_response('leaderboard.html', {'achievements': achievements,})
