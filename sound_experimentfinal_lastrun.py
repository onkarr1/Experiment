#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on May 14, 2024, at 19:09
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code_6
continueRoutine = True
# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'sound_experimentfinal'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\fgraz\\OneDrive\\Desktop\\phase1\\Experiment\\sound_experimentfinal_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.WARNING)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.WARNING)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1536, 864], fullscr=True, screen=1,
            winType='pyglet', allowStencil=True,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = True
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='event')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='Pyglet')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Instructions" ---
    Welcome = visual.TextStim(win=win, name='Welcome',
        text='Welcome!\n\n\nIn this experiment, you will see balls moving horizontally as shown next',
        font='Open Sans',
        pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard()
    PressKey = visual.TextStim(win=win, name='PressKey',
        text='Press the space bar to continue',
        font='Open Sans',
        pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "BallMovingExplanation" ---
    Wall = visual.Rect(
        win=win, name='Wall',
        width=(1.5, 1)[0], height=(1.5, 1)[1],
        ori=0.0, pos=(-0.1, 0), anchor='center-left',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=0.85, depth=0.0, interpolate=True)
    Circle = visual.ShapeStim(
        win=win, name='Circle',
        size=[1.0, 1.0], vertices='circle',
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
        opacity=None, depth=-1.0, interpolate=True)
    wall_front_2 = visual.Rect(
        win=win, name='wall_front_2',
        width=(1.5, 1)[0], height=(1.5, 1)[1],
        ori=0.0, pos=(-0.1, 0), anchor='center-left',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=0.5, depth=-2.0, interpolate=True)
    Presstoendroutine = keyboard.Keyboard()
    BallHidden = visual.TextStim(win=win, name='BallHidden',
        text='The ball will move at a constant speed, but  a black screen will hide part of the movement.',
        font='Open Sans',
        pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    BallHidden_2 = visual.TextStim(win=win, name='BallHidden_2',
        text='In the actual experiment, the screen will completely hide the ball.',
        font='Open Sans',
        pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    Presskey = visual.TextStim(win=win, name='Presskey',
        text='Press the space bar to continue',
        font='Open Sans',
        pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    sound_1 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
        name='sound_1')
    sound_1.setVolume(1.0)
    # Run 'Begin Experiment' code from code_8
    win_size = win.size
    extremeLeft = -(win.size[0]/win.size[1])/2
    
    # --- Initialize components for Routine "Target" ---
    polygon_5 = visual.Rect(
        win=win, name='polygon_5',
        width=(1.5, 1)[0], height=(1.5, 1)[1],
        ori=0.0, pos=(-0.1, 0), anchor='center-left',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=0.0, interpolate=True)
    Target_1 = visual.ShapeStim(
        win=win, name='Target_1',
        size=(0.01, 0.01), vertices='circle',
        ori=0.0, pos=(0.5, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
        opacity=None, depth=-1.0, interpolate=True)
    key_resp_6 = keyboard.Keyboard()
    text_11 = visual.TextStim(win=win, name='text_11',
        text='You will see a target on the right hand of the screen.',
        font='Open Sans',
        pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    text_10 = visual.TextStim(win=win, name='text_10',
        text='Press the space bar to continue',
        font='Open Sans',
        pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "Finalballposition" ---
    key_resp_5 = keyboard.Keyboard()
    wall_back = visual.Rect(
        win=win, name='wall_back',
        width=(1.5, 1)[0], height=(1.5, 1)[1],
        ori=0.0, pos=(-0.1, 0), anchor='center-left',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=1.0, depth=-1.0, interpolate=True)
    ball = visual.ShapeStim(
        win=win, name='ball',
        size=[1.0, 1.0], vertices='circle',
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
        opacity=None, depth=-2.0, interpolate=True)
    wall_front = visual.Rect(
        win=win, name='wall_front',
        width=(1.5, 1)[0], height=(1.5, 1)[1],
        ori=0.0, pos=(-0.1, 0), anchor='center-left',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=0.5, depth=-3.0, interpolate=True)
    StopTarget = visual.TextStim(win=win, name='StopTarget',
        text='Press SPACE when the ball is EXACTLY ON THE TARGET\n',
        font='Open Sans',
        pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    Rewards = visual.TextStim(win=win, name='Rewards',
        text='Focus on the ACCURACY of your responses.\nPlease take breaks only when indicated in the experiment prompts.\n',
        font='Open Sans',
        pos=(0, -0.25), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    text_5 = visual.TextStim(win=win, name='text_5',
        text='Press the space bar to continue',
        font='Open Sans',
        pos=(0, -.4), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    aim = visual.ShapeStim(
        win=win, name='aim',
        size=(0.01, 0.01), vertices='circle',
        ori=0.0, pos=(0.5, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
        opacity=None, depth=-7.0, interpolate=True)
    sound_3 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
        name='sound_3')
    sound_3.setVolume(1.0)
    # Run 'Begin Experiment' code from code_9
    win_size = win.size
    extremeLeft = -(win.size[0]/win.size[1])/2
    # Run 'Begin Experiment' code from code_moving
    current_time = 0
    ball_stopped = False
    
    
    # --- Initialize components for Routine "Practice" ---
    key_resp_7 = keyboard.Keyboard()
    PacticePrompt = visual.TextStim(win=win, name='PacticePrompt',
        text='You will start a practice trial',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    text_12 = visual.TextStim(win=win, name='text_12',
        text='Press the space bar to continue',
        font='Open Sans',
        pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "BallMoving" ---
    Circle_2 = visual.ShapeStim(
        win=win, name='Circle_2',
        size=[1.0, 1.0], vertices='circle',
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
        opacity=None, depth=0.0, interpolate=True)
    Wall_2 = visual.Rect(
        win=win, name='Wall_2',
        width=(1.5, 1)[0], height=(1.5, 1)[1],
        ori=0.0, pos=(-0.1, 0), anchor='center-left',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=1.0, depth=-1.0, interpolate=True)
    Target_2 = visual.ShapeStim(
        win=win, name='Target_2',
        size=(0.01, 0.01), vertices='circle',
        ori=0.0, pos=(0.5, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
        opacity=None, depth=-2.0, interpolate=True)
    Presstoendroutine_2 = keyboard.Keyboard()
    sound_2 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
        name='sound_2')
    sound_2.setVolume(1.0)
    # Run 'Begin Experiment' code from code_10
    win_size = win.size
    extremeLeft = -(win.size[0]/win.size[1])/2
    
    # --- Initialize components for Routine "Rest" ---
    Wall_3 = visual.Rect(
        win=win, name='Wall_3',
        width=(1.5, 1)[0], height=(1.5, 1)[1],
        ori=0.0, pos=(-0.1, 0), anchor='center-left',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=1.0, depth=0.0, interpolate=True)
    Target_3 = visual.ShapeStim(
        win=win, name='Target_3',
        size=(0.01, 0.01), vertices='circle',
        ori=0.0, pos=(0.5, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
        opacity=None, depth=-1.0, interpolate=True)
    
    # --- Initialize components for Routine "Continue" ---
    text = visual.TextStim(win=win, name='text',
        text='Are you ready to begin?\n\nPress Y or N',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "presstoBegin" ---
    key_resp_3 = keyboard.Keyboard()
    text_2 = visual.TextStim(win=win, name='text_2',
        text='Press the space bar to begin the experiment:',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "BallMoving" ---
    Circle_2 = visual.ShapeStim(
        win=win, name='Circle_2',
        size=[1.0, 1.0], vertices='circle',
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
        opacity=None, depth=0.0, interpolate=True)
    Wall_2 = visual.Rect(
        win=win, name='Wall_2',
        width=(1.5, 1)[0], height=(1.5, 1)[1],
        ori=0.0, pos=(-0.1, 0), anchor='center-left',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=1.0, depth=-1.0, interpolate=True)
    Target_2 = visual.ShapeStim(
        win=win, name='Target_2',
        size=(0.01, 0.01), vertices='circle',
        ori=0.0, pos=(0.5, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
        opacity=None, depth=-2.0, interpolate=True)
    Presstoendroutine_2 = keyboard.Keyboard()
    sound_2 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
        name='sound_2')
    sound_2.setVolume(1.0)
    # Run 'Begin Experiment' code from code_10
    win_size = win.size
    extremeLeft = -(win.size[0]/win.size[1])/2
    
    # --- Initialize components for Routine "Rest" ---
    Wall_3 = visual.Rect(
        win=win, name='Wall_3',
        width=(1.5, 1)[0], height=(1.5, 1)[1],
        ori=0.0, pos=(-0.1, 0), anchor='center-left',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=1.0, depth=0.0, interpolate=True)
    Target_3 = visual.ShapeStim(
        win=win, name='Target_3',
        size=(0.01, 0.01), vertices='circle',
        ori=0.0, pos=(0.5, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
        opacity=None, depth=-1.0, interpolate=True)
    
    # --- Initialize components for Routine "ShortRestwithTarget" ---
    key_resp_9 = keyboard.Keyboard()
    wall_back_3 = visual.Rect(
        win=win, name='wall_back_3',
        width=(1.5, 1)[0], height=(1.5, 1)[1],
        ori=0.0, pos=(-0.1, 0), anchor='center-left',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=1.0, depth=-1.0, interpolate=True)
    StopTarget_3 = visual.TextStim(win=win, name='StopTarget_3',
        text='Take a short break\n',
        font='Open Sans',
        pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_7 = visual.TextStim(win=win, name='text_7',
        text='Press the space bar to continue',
        font='Open Sans',
        pos=(0, -.4), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    aim_3 = visual.ShapeStim(
        win=win, name='aim_3',
        size=(0.01, 0.01), vertices='circle',
        ori=0.0, pos=(0.5, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
        opacity=None, depth=-4.0, interpolate=True)
    
    # --- Initialize components for Routine "SessionBreak" ---
    SessionBreak_2 = visual.TextStim(win=win, name='SessionBreak_2',
        text='Way to go!\n\nTake a longer break until you are ready to continue.',
        font='Open Sans',
        pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_4 = keyboard.Keyboard()
    Presskey_2 = visual.TextStim(win=win, name='Presskey_2',
        text='Press the space key to continue',
        font='Open Sans',
        pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "SurveyEnd" ---
    Survey = visual.TextStim(win=win, name='Survey',
        text='Congratulations! \nYou completed the experiment. \nWe just have a few more questions:\n',
        font='Open Sans',
        pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Speeds = visual.TextBox2(
         win, text='1) How many different speeds did you identify? \n', placeholder=None, font='Arial',
         pos=(-0.7, 0.15),     letterHeight=0.04,
         size=(1.4, 0.2), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center-left',
         anchor='center-left', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='Speeds',
         depth=-1, autoLog=True,
    )
    Strategy = visual.TextBox2(
         win, text='2) Did you use any particular strategy to estimate the ball movement?  \n', placeholder=None, font='Arial',
         pos=(-0.7, 0.05),     letterHeight=0.04,
         size=(1.4, 0.2), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center-left',
         anchor='center-left', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='Strategy',
         depth=-2, autoLog=True,
    )
    Purpose = visual.TextBox2(
         win, text='3) What do you think is the purpose of the experiment?  \n', placeholder=None, font='Arial',
         pos=(-0.7, -0.05),     letterHeight=0.04,
         size=(1.4, 0.2), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center-left',
         anchor='center-left', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='Purpose',
         depth=-3, autoLog=True,
    )
    Age = visual.TextBox2(
         win, text='4) Please write down your age\n', placeholder=None, font='Arial',
         pos=(-0.7, -0.15),     letterHeight=0.04,
         size=(1.4, 0.2), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center-left',
         anchor='center-left', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='Age',
         depth=-4, autoLog=True,
    )
    Gender = visual.TextBox2(
         win, text='5) Please state your gender (M) or (F)\n', placeholder=None, font='Arial',
         pos=(-0.7, -0.25),     letterHeight=0.04,
         size=(1.4, 0.2), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center-left',
         anchor='center-left', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='Gender',
         depth=-5, autoLog=True,
    )
    PressCTRL = visual.TextStim(win=win, name='PressCTRL',
        text='Press the CTRL key to continue',
        font='Open Sans',
        pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    
    # --- Initialize components for Routine "Thank_you" ---
    Thankyou = visual.TextStim(win=win, name='Thankyou',
        text='Thank you for your participation\n\n\n\nPlease press Esc to end the experiment.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "Instructions" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instructions.started', globalClock.getTime())
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    InstructionsComponents = [Welcome, key_resp_2, PressKey]
    for thisComponent in InstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Welcome* updates
        
        # if Welcome is starting this frame...
        if Welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Welcome.frameNStart = frameN  # exact frame index
            Welcome.tStart = t  # local t and not account for scr refresh
            Welcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Welcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Welcome.started')
            # update status
            Welcome.status = STARTED
            Welcome.setAutoDraw(True)
        
        # if Welcome is active this frame...
        if Welcome.status == STARTED:
            # update params
            pass
        
        # *key_resp_2* updates
        waitOnFlip = False
        
        # if key_resp_2 is starting this frame...
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            # update status
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *PressKey* updates
        
        # if PressKey is starting this frame...
        if PressKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PressKey.frameNStart = frameN  # exact frame index
            PressKey.tStart = t  # local t and not account for scr refresh
            PressKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PressKey, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PressKey.started')
            # update status
            PressKey.status = STARTED
            PressKey.setAutoDraw(True)
        
        # if PressKey is active this frame...
        if PressKey.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions" ---
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instructions.stopped', globalClock.getTime())
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.addData('key_resp_2.duration', key_resp_2.duration)
    thisExp.nextEntry()
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "BallMovingExplanation" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BallMovingExplanation.started', globalClock.getTime())
    Circle.setSize((0.2, 0.2))
    Presstoendroutine.keys = []
    Presstoendroutine.rt = []
    _Presstoendroutine_allKeys = []
    sound_1.setSound('A', secs=10, hamming=True)
    sound_1.setVolume(1.0, log=False)
    sound_1.seek(0)
    # keep track of which components have finished
    BallMovingExplanationComponents = [Wall, Circle, wall_front_2, Presstoendroutine, BallHidden, BallHidden_2, Presskey, sound_1]
    for thisComponent in BallMovingExplanationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BallMovingExplanation" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Wall* updates
        
        # if Wall is starting this frame...
        if Wall.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            Wall.frameNStart = frameN  # exact frame index
            Wall.tStart = t  # local t and not account for scr refresh
            Wall.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Wall, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Wall.started')
            # update status
            Wall.status = STARTED
            Wall.setAutoDraw(True)
        
        # if Wall is active this frame...
        if Wall.status == STARTED:
            # update params
            pass
        
        # *Circle* updates
        
        # if Circle is starting this frame...
        if Circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Circle.frameNStart = frameN  # exact frame index
            Circle.tStart = t  # local t and not account for scr refresh
            Circle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Circle, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Circle.started')
            # update status
            Circle.status = STARTED
            Circle.setAutoDraw(True)
        
        # if Circle is active this frame...
        if Circle.status == STARTED:
            # update params
            Circle.setPos((extremeLeft-0.1 + t/2, 0), log=False)
        
        # *wall_front_2* updates
        
        # if wall_front_2 is starting this frame...
        if wall_front_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            wall_front_2.frameNStart = frameN  # exact frame index
            wall_front_2.tStart = t  # local t and not account for scr refresh
            wall_front_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wall_front_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'wall_front_2.started')
            # update status
            wall_front_2.status = STARTED
            wall_front_2.setAutoDraw(True)
        
        # if wall_front_2 is active this frame...
        if wall_front_2.status == STARTED:
            # update params
            pass
        
        # *Presstoendroutine* updates
        waitOnFlip = False
        
        # if Presstoendroutine is starting this frame...
        if Presstoendroutine.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            Presstoendroutine.frameNStart = frameN  # exact frame index
            Presstoendroutine.tStart = t  # local t and not account for scr refresh
            Presstoendroutine.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Presstoendroutine, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Presstoendroutine.started')
            # update status
            Presstoendroutine.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Presstoendroutine.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Presstoendroutine.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Presstoendroutine.status == STARTED and not waitOnFlip:
            theseKeys = Presstoendroutine.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _Presstoendroutine_allKeys.extend(theseKeys)
            if len(_Presstoendroutine_allKeys):
                Presstoendroutine.keys = _Presstoendroutine_allKeys[-1].name  # just the last key pressed
                Presstoendroutine.rt = _Presstoendroutine_allKeys[-1].rt
                Presstoendroutine.duration = _Presstoendroutine_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *BallHidden* updates
        
        # if BallHidden is starting this frame...
        if BallHidden.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            BallHidden.frameNStart = frameN  # exact frame index
            BallHidden.tStart = t  # local t and not account for scr refresh
            BallHidden.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BallHidden, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'BallHidden.started')
            # update status
            BallHidden.status = STARTED
            BallHidden.setAutoDraw(True)
        
        # if BallHidden is active this frame...
        if BallHidden.status == STARTED:
            # update params
            pass
        
        # *BallHidden_2* updates
        
        # if BallHidden_2 is starting this frame...
        if BallHidden_2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            BallHidden_2.frameNStart = frameN  # exact frame index
            BallHidden_2.tStart = t  # local t and not account for scr refresh
            BallHidden_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BallHidden_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'BallHidden_2.started')
            # update status
            BallHidden_2.status = STARTED
            BallHidden_2.setAutoDraw(True)
        
        # if BallHidden_2 is active this frame...
        if BallHidden_2.status == STARTED:
            # update params
            pass
        
        # *Presskey* updates
        
        # if Presskey is starting this frame...
        if Presskey.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Presskey.frameNStart = frameN  # exact frame index
            Presskey.tStart = t  # local t and not account for scr refresh
            Presskey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Presskey, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Presskey.started')
            # update status
            Presskey.status = STARTED
            Presskey.setAutoDraw(True)
        
        # if Presskey is active this frame...
        if Presskey.status == STARTED:
            # update params
            pass
        
        # if sound_1 is starting this frame...
        if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_1.started', tThisFlipGlobal)
            # update status
            sound_1.status = STARTED
            sound_1.play(when=win)  # sync with win flip
        
        # if sound_1 is stopping this frame...
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sound_1.stopped')
                # update status
                sound_1.status = FINISHED
                sound_1.stop()
        # update sound_1 status according to whether it's playing
        if sound_1.isPlaying:
            sound_1.status = STARTED
        elif sound_1.isFinished:
            sound_1.status = FINISHED
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BallMovingExplanationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BallMovingExplanation" ---
    for thisComponent in BallMovingExplanationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BallMovingExplanation.stopped', globalClock.getTime())
    # check responses
    if Presstoendroutine.keys in ['', [], None]:  # No response was made
        Presstoendroutine.keys = None
    thisExp.addData('Presstoendroutine.keys',Presstoendroutine.keys)
    if Presstoendroutine.keys != None:  # we had a response
        thisExp.addData('Presstoendroutine.rt', Presstoendroutine.rt)
        thisExp.addData('Presstoendroutine.duration', Presstoendroutine.duration)
    thisExp.nextEntry()
    sound_1.pause()  # ensure sound has stopped at end of Routine
    # the Routine "BallMovingExplanation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Target" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Target.started', globalClock.getTime())
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # keep track of which components have finished
    TargetComponents = [polygon_5, Target_1, key_resp_6, text_11, text_10]
    for thisComponent in TargetComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Target" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_5* updates
        
        # if polygon_5 is starting this frame...
        if polygon_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_5.frameNStart = frameN  # exact frame index
            polygon_5.tStart = t  # local t and not account for scr refresh
            polygon_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_5.started')
            # update status
            polygon_5.status = STARTED
            polygon_5.setAutoDraw(True)
        
        # if polygon_5 is active this frame...
        if polygon_5.status == STARTED:
            # update params
            pass
        
        # *Target_1* updates
        
        # if Target_1 is starting this frame...
        if Target_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Target_1.frameNStart = frameN  # exact frame index
            Target_1.tStart = t  # local t and not account for scr refresh
            Target_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Target_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Target_1.started')
            # update status
            Target_1.status = STARTED
            Target_1.setAutoDraw(True)
        
        # if Target_1 is active this frame...
        if Target_1.status == STARTED:
            # update params
            pass
        
        # *key_resp_6* updates
        waitOnFlip = False
        
        # if key_resp_6 is starting this frame...
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_6.started')
            # update status
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                key_resp_6.duration = _key_resp_6_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_11* updates
        
        # if text_11 is starting this frame...
        if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_11.frameNStart = frameN  # exact frame index
            text_11.tStart = t  # local t and not account for scr refresh
            text_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_11.started')
            # update status
            text_11.status = STARTED
            text_11.setAutoDraw(True)
        
        # if text_11 is active this frame...
        if text_11.status == STARTED:
            # update params
            pass
        
        # *text_10* updates
        
        # if text_10 is starting this frame...
        if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_10.frameNStart = frameN  # exact frame index
            text_10.tStart = t  # local t and not account for scr refresh
            text_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_10.started')
            # update status
            text_10.status = STARTED
            text_10.setAutoDraw(True)
        
        # if text_10 is active this frame...
        if text_10.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TargetComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Target" ---
    for thisComponent in TargetComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Target.stopped', globalClock.getTime())
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    thisExp.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        thisExp.addData('key_resp_6.rt', key_resp_6.rt)
        thisExp.addData('key_resp_6.duration', key_resp_6.duration)
    thisExp.nextEntry()
    # the Routine "Target" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Finalballposition" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Finalballposition.started', globalClock.getTime())
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    ball.setSize((0.2, 0.2))
    sound_3.setSound('A', secs=10, hamming=True)
    sound_3.setVolume(1.0, log=False)
    sound_3.seek(0)
    # Run 'Begin Routine' code from code_moving
    sound_3.setVolume(0)
    # keep track of which components have finished
    FinalballpositionComponents = [key_resp_5, wall_back, ball, wall_front, StopTarget, Rewards, text_5, aim, sound_3]
    for thisComponent in FinalballpositionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Finalballposition" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_5* updates
        waitOnFlip = False
        
        # if key_resp_5 is starting this frame...
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 4.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_5.started')
            # update status
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                key_resp_5.duration = _key_resp_5_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *wall_back* updates
        
        # if wall_back is starting this frame...
        if wall_back.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wall_back.frameNStart = frameN  # exact frame index
            wall_back.tStart = t  # local t and not account for scr refresh
            wall_back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wall_back, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'wall_back.started')
            # update status
            wall_back.status = STARTED
            wall_back.setAutoDraw(True)
        
        # if wall_back is active this frame...
        if wall_back.status == STARTED:
            # update params
            pass
        
        # *ball* updates
        
        # if ball is starting this frame...
        if ball.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ball.frameNStart = frameN  # exact frame index
            ball.tStart = t  # local t and not account for scr refresh
            ball.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ball, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ball.started')
            # update status
            ball.status = STARTED
            ball.setAutoDraw(True)
        
        # if ball is active this frame...
        if ball.status == STARTED:
            # update params
            ball.setPos(((extremeLeft-0.1) + current_time, 0), log=False)
        
        # *wall_front* updates
        
        # if wall_front is starting this frame...
        if wall_front.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wall_front.frameNStart = frameN  # exact frame index
            wall_front.tStart = t  # local t and not account for scr refresh
            wall_front.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wall_front, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'wall_front.started')
            # update status
            wall_front.status = STARTED
            wall_front.setAutoDraw(True)
        
        # if wall_front is active this frame...
        if wall_front.status == STARTED:
            # update params
            pass
        
        # *StopTarget* updates
        
        # if StopTarget is starting this frame...
        if StopTarget.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StopTarget.frameNStart = frameN  # exact frame index
            StopTarget.tStart = t  # local t and not account for scr refresh
            StopTarget.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StopTarget, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StopTarget.started')
            # update status
            StopTarget.status = STARTED
            StopTarget.setAutoDraw(True)
        
        # if StopTarget is active this frame...
        if StopTarget.status == STARTED:
            # update params
            pass
        
        # *Rewards* updates
        
        # if Rewards is starting this frame...
        if Rewards.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            Rewards.frameNStart = frameN  # exact frame index
            Rewards.tStart = t  # local t and not account for scr refresh
            Rewards.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Rewards, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Rewards.started')
            # update status
            Rewards.status = STARTED
            Rewards.setAutoDraw(True)
        
        # if Rewards is active this frame...
        if Rewards.status == STARTED:
            # update params
            pass
        
        # *text_5* updates
        
        # if text_5 is starting this frame...
        if text_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_5.started')
            # update status
            text_5.status = STARTED
            text_5.setAutoDraw(True)
        
        # if text_5 is active this frame...
        if text_5.status == STARTED:
            # update params
            pass
        
        # *aim* updates
        
        # if aim is starting this frame...
        if aim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            aim.frameNStart = frameN  # exact frame index
            aim.tStart = t  # local t and not account for scr refresh
            aim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(aim, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'aim.started')
            # update status
            aim.status = STARTED
            aim.setAutoDraw(True)
        
        # if aim is active this frame...
        if aim.status == STARTED:
            # update params
            pass
        
        # if sound_3 is starting this frame...
        if sound_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_3.frameNStart = frameN  # exact frame index
            sound_3.tStart = t  # local t and not account for scr refresh
            sound_3.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_3.started', tThisFlipGlobal)
            # update status
            sound_3.status = STARTED
            sound_3.play(when=win)  # sync with win flip
        
        # if sound_3 is stopping this frame...
        if sound_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_3.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                sound_3.tStop = t  # not accounting for scr refresh
                sound_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sound_3.stopped')
                # update status
                sound_3.status = FINISHED
                sound_3.stop()
        # update sound_3 status according to whether it's playing
        if sound_3.isPlaying:
            sound_3.status = STARTED
        elif sound_3.isFinished:
            sound_3.status = FINISHED
        # Run 'Each Frame' code from code_moving
        if (not ball_stopped) and ball.pos[0] < 0.5:
            current_time = t
            sound_3.setVolume(1)
        else:
            current_time = -(extremeLeft-0.1)+0.5
            wall_front.opacity = 0
            ball_stopped = True
            sound_3.setVolume(0)
        
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FinalballpositionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Finalballposition" ---
    for thisComponent in FinalballpositionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Finalballposition.stopped', globalClock.getTime())
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    thisExp.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        thisExp.addData('key_resp_5.rt', key_resp_5.rt)
        thisExp.addData('key_resp_5.duration', key_resp_5.duration)
    thisExp.nextEntry()
    sound_3.pause()  # ensure sound has stopped at end of Routine
    # the Routine "Finalballposition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=100.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            globals()[paramName] = thisTrial_2[paramName]
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                globals()[paramName] = thisTrial_2[paramName]
        
        # --- Prepare to start Routine "Practice" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Practice.started', globalClock.getTime())
        key_resp_7.keys = []
        key_resp_7.rt = []
        _key_resp_7_allKeys = []
        # keep track of which components have finished
        PracticeComponents = [key_resp_7, PacticePrompt, text_12]
        for thisComponent in PracticeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Practice" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_7* updates
            waitOnFlip = False
            
            # if key_resp_7 is starting this frame...
            if key_resp_7.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                key_resp_7.frameNStart = frameN  # exact frame index
                key_resp_7.tStart = t  # local t and not account for scr refresh
                key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_7.started')
                # update status
                key_resp_7.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_7.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_7.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_7_allKeys.extend(theseKeys)
                if len(_key_resp_7_allKeys):
                    key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                    key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                    key_resp_7.duration = _key_resp_7_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *PacticePrompt* updates
            
            # if PacticePrompt is starting this frame...
            if PacticePrompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PacticePrompt.frameNStart = frameN  # exact frame index
                PacticePrompt.tStart = t  # local t and not account for scr refresh
                PacticePrompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PacticePrompt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'PacticePrompt.started')
                # update status
                PacticePrompt.status = STARTED
                PacticePrompt.setAutoDraw(True)
            
            # if PacticePrompt is active this frame...
            if PacticePrompt.status == STARTED:
                # update params
                pass
            
            # *text_12* updates
            
            # if text_12 is starting this frame...
            if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_12.frameNStart = frameN  # exact frame index
                text_12.tStart = t  # local t and not account for scr refresh
                text_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_12.started')
                # update status
                text_12.status = STARTED
                text_12.setAutoDraw(True)
            
            # if text_12 is active this frame...
            if text_12.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Practice" ---
        for thisComponent in PracticeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Practice.stopped', globalClock.getTime())
        # check responses
        if key_resp_7.keys in ['', [], None]:  # No response was made
            key_resp_7.keys = None
        trials_2.addData('key_resp_7.keys',key_resp_7.keys)
        if key_resp_7.keys != None:  # we had a response
            trials_2.addData('key_resp_7.rt', key_resp_7.rt)
            trials_2.addData('key_resp_7.duration', key_resp_7.duration)
        # the Routine "Practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('MovementParameters.xlsx', selection='0:3'),
            seed=None, name='trials')
        thisExp.addLoop(trials)  # add the loop to the experiment
        thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        for thisTrial in trials:
            currentLoop = trials
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial:
                    globals()[paramName] = thisTrial[paramName]
            
            # --- Prepare to start Routine "BallMoving" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('BallMoving.started', globalClock.getTime())
            Circle_2.setSize((0.2, 0.2))
            Presstoendroutine_2.keys = []
            Presstoendroutine_2.rt = []
            _Presstoendroutine_2_allKeys = []
            sound_2.setSound(frequencyvalue, secs=10, hamming=True)
            sound_2.setVolume(1.0, log=False)
            sound_2.seek(0)
            # Run 'Begin Routine' code from code_5
            final_position = None
            # Run 'Begin Routine' code from code_7
            sound_2.setVolume(0)
            # keep track of which components have finished
            BallMovingComponents = [Circle_2, Wall_2, Target_2, Presstoendroutine_2, sound_2]
            for thisComponent in BallMovingComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "BallMoving" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Circle_2* updates
                
                # if Circle_2 is starting this frame...
                if Circle_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Circle_2.frameNStart = frameN  # exact frame index
                    Circle_2.tStart = t  # local t and not account for scr refresh
                    Circle_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Circle_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Circle_2.started')
                    # update status
                    Circle_2.status = STARTED
                    Circle_2.setAutoDraw(True)
                
                # if Circle_2 is active this frame...
                if Circle_2.status == STARTED:
                    # update params
                    Circle_2.setPos(((extremeLeft-0.1)+t*Speed, 0), log=False)
                
                # *Wall_2* updates
                
                # if Wall_2 is starting this frame...
                if Wall_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Wall_2.frameNStart = frameN  # exact frame index
                    Wall_2.tStart = t  # local t and not account for scr refresh
                    Wall_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Wall_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Wall_2.started')
                    # update status
                    Wall_2.status = STARTED
                    Wall_2.setAutoDraw(True)
                
                # if Wall_2 is active this frame...
                if Wall_2.status == STARTED:
                    # update params
                    pass
                
                # if Wall_2 is stopping this frame...
                if Wall_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Wall_2.tStartRefresh + 10-frameTolerance:
                        # keep track of stop time/frame for later
                        Wall_2.tStop = t  # not accounting for scr refresh
                        Wall_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Wall_2.stopped')
                        # update status
                        Wall_2.status = FINISHED
                        Wall_2.setAutoDraw(False)
                
                # *Target_2* updates
                
                # if Target_2 is starting this frame...
                if Target_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Target_2.frameNStart = frameN  # exact frame index
                    Target_2.tStart = t  # local t and not account for scr refresh
                    Target_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Target_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Target_2.started')
                    # update status
                    Target_2.status = STARTED
                    Target_2.setAutoDraw(True)
                
                # if Target_2 is active this frame...
                if Target_2.status == STARTED:
                    # update params
                    pass
                
                # *Presstoendroutine_2* updates
                waitOnFlip = False
                
                # if Presstoendroutine_2 is starting this frame...
                if Presstoendroutine_2.status == NOT_STARTED and tThisFlip >= 1/Speed-frameTolerance:
                    # keep track of start time/frame for later
                    Presstoendroutine_2.frameNStart = frameN  # exact frame index
                    Presstoendroutine_2.tStart = t  # local t and not account for scr refresh
                    Presstoendroutine_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Presstoendroutine_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Presstoendroutine_2.started')
                    # update status
                    Presstoendroutine_2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(Presstoendroutine_2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(Presstoendroutine_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if Presstoendroutine_2.status == STARTED and not waitOnFlip:
                    theseKeys = Presstoendroutine_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _Presstoendroutine_2_allKeys.extend(theseKeys)
                    if len(_Presstoendroutine_2_allKeys):
                        Presstoendroutine_2.keys = _Presstoendroutine_2_allKeys[-1].name  # just the last key pressed
                        Presstoendroutine_2.rt = _Presstoendroutine_2_allKeys[-1].rt
                        Presstoendroutine_2.duration = _Presstoendroutine_2_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # if sound_2 is starting this frame...
                if sound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    sound_2.frameNStart = frameN  # exact frame index
                    sound_2.tStart = t  # local t and not account for scr refresh
                    sound_2.tStartRefresh = tThisFlipGlobal  # on global time
                    # add timestamp to datafile
                    thisExp.addData('sound_2.started', tThisFlipGlobal)
                    # update status
                    sound_2.status = STARTED
                    sound_2.play(when=win)  # sync with win flip
                
                # if sound_2 is stopping this frame...
                if sound_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > sound_2.tStartRefresh + 10-frameTolerance:
                        # keep track of stop time/frame for later
                        sound_2.tStop = t  # not accounting for scr refresh
                        sound_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'sound_2.stopped')
                        # update status
                        sound_2.status = FINISHED
                        sound_2.stop()
                # update sound_2 status according to whether it's playing
                if sound_2.isPlaying:
                    sound_2.status = STARTED
                elif sound_2.isFinished:
                    sound_2.status = FINISHED
                # Run 'Each Frame' code from code_7
                if ball.pos[0] > -1.1:
                    sound_2.setVolume(1)
                else:
                    sound_2.setVolume(0)
                
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in BallMovingComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "BallMoving" ---
            for thisComponent in BallMovingComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('BallMoving.stopped', globalClock.getTime())
            # check responses
            if Presstoendroutine_2.keys in ['', [], None]:  # No response was made
                Presstoendroutine_2.keys = None
            trials.addData('Presstoendroutine_2.keys',Presstoendroutine_2.keys)
            if Presstoendroutine_2.keys != None:  # we had a response
                trials.addData('Presstoendroutine_2.rt', Presstoendroutine_2.rt)
                trials.addData('Presstoendroutine_2.duration', Presstoendroutine_2.duration)
            sound_2.pause()  # ensure sound has stopped at end of Routine
            # Run 'End Routine' code from code_5
            # Calculate the final position adjusted for the radius
            final_position = (Circle_2.pos[0] - 0.1, Circle_2.pos[1])
            
            # Output the adjusted final position to the data file
            thisExp.addData('final_position_x', final_position[0])
            thisExp.addData('final_position_y', final_position[1])
            # the Routine "BallMoving" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "Rest" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('Rest.started', globalClock.getTime())
            # keep track of which components have finished
            RestComponents = [Wall_3, Target_3]
            for thisComponent in RestComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Rest" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Wall_3* updates
                
                # if Wall_3 is starting this frame...
                if Wall_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    Wall_3.frameNStart = frameN  # exact frame index
                    Wall_3.tStart = t  # local t and not account for scr refresh
                    Wall_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Wall_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Wall_3.started')
                    # update status
                    Wall_3.status = STARTED
                    Wall_3.setAutoDraw(True)
                
                # if Wall_3 is active this frame...
                if Wall_3.status == STARTED:
                    # update params
                    pass
                
                # if Wall_3 is stopping this frame...
                if Wall_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Wall_3.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        Wall_3.tStop = t  # not accounting for scr refresh
                        Wall_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Wall_3.stopped')
                        # update status
                        Wall_3.status = FINISHED
                        Wall_3.setAutoDraw(False)
                
                # *Target_3* updates
                
                # if Target_3 is starting this frame...
                if Target_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Target_3.frameNStart = frameN  # exact frame index
                    Target_3.tStart = t  # local t and not account for scr refresh
                    Target_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Target_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Target_3.started')
                    # update status
                    Target_3.status = STARTED
                    Target_3.setAutoDraw(True)
                
                # if Target_3 is active this frame...
                if Target_3.status == STARTED:
                    # update params
                    pass
                
                # if Target_3 is stopping this frame...
                if Target_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Target_3.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        Target_3.tStop = t  # not accounting for scr refresh
                        Target_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Target_3.stopped')
                        # update status
                        Target_3.status = FINISHED
                        Target_3.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in RestComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Rest" ---
            for thisComponent in RestComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('Rest.stopped', globalClock.getTime())
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'trials'
        
        
        # --- Prepare to start Routine "Continue" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Continue.started', globalClock.getTime())
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        ContinueComponents = [text, key_resp]
        for thisComponent in ContinueComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Continue" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code
            # Each Frame
            keys = key_resp.getKeys()
            
            if keys:
                if keys[0].name == 'n':
                    continueRoutine = False  # Set continueRoutine to False to end the routine
                elif keys[0].name == 'y':
                    trials_2.finished = True  # End the entire loop
                    continueRoutine = False 
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['y','n'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ContinueComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Continue" ---
        for thisComponent in ContinueComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Continue.stopped', globalClock.getTime())
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        trials_2.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials_2.addData('key_resp.rt', key_resp.rt)
            trials_2.addData('key_resp.duration', key_resp.duration)
        # the Routine "Continue" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 100.0 repeats of 'trials_2'
    
    
    # --- Prepare to start Routine "presstoBegin" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('presstoBegin.started', globalClock.getTime())
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    presstoBeginComponents = [key_resp_3, text_2]
    for thisComponent in presstoBeginComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "presstoBegin" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_3* updates
        waitOnFlip = False
        
        # if key_resp_3 is starting this frame...
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3.started')
            # update status
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_2* updates
        
        # if text_2 is starting this frame...
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            # update status
            text_2.status = STARTED
            text_2.setAutoDraw(True)
        
        # if text_2 is active this frame...
        if text_2.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in presstoBeginComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "presstoBegin" ---
    for thisComponent in presstoBeginComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('presstoBegin.stopped', globalClock.getTime())
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    thisExp.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        thisExp.addData('key_resp_3.rt', key_resp_3.rt)
        thisExp.addData('key_resp_3.duration', key_resp_3.duration)
    thisExp.nextEntry()
    # the Routine "presstoBegin" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_4sessions = data.TrialHandler(nReps=4.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_4sessions')
    thisExp.addLoop(trials_4sessions)  # add the loop to the experiment
    thisTrials_4session = trials_4sessions.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_4session.rgb)
    if thisTrials_4session != None:
        for paramName in thisTrials_4session:
            globals()[paramName] = thisTrials_4session[paramName]
    
    for thisTrials_4session in trials_4sessions:
        currentLoop = trials_4sessions
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_4session.rgb)
        if thisTrials_4session != None:
            for paramName in thisTrials_4session:
                globals()[paramName] = thisTrials_4session[paramName]
        
        # set up handler to look after randomisation of conditions etc
        trials_6times = data.TrialHandler(nReps=6.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_6times')
        thisExp.addLoop(trials_6times)  # add the loop to the experiment
        thisTrials_6time = trials_6times.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_6time.rgb)
        if thisTrials_6time != None:
            for paramName in thisTrials_6time:
                globals()[paramName] = thisTrials_6time[paramName]
        
        for thisTrials_6time in trials_6times:
            currentLoop = trials_6times
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_6time.rgb)
            if thisTrials_6time != None:
                for paramName in thisTrials_6time:
                    globals()[paramName] = thisTrials_6time[paramName]
            
            # set up handler to look after randomisation of conditions etc
            trials_2_16times = data.TrialHandler(nReps=2.0, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions('MovementParameters.xlsx'),
                seed=None, name='trials_2_16times')
            thisExp.addLoop(trials_2_16times)  # add the loop to the experiment
            thisTrials_2_16time = trials_2_16times.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_2_16time.rgb)
            if thisTrials_2_16time != None:
                for paramName in thisTrials_2_16time:
                    globals()[paramName] = thisTrials_2_16time[paramName]
            
            for thisTrials_2_16time in trials_2_16times:
                currentLoop = trials_2_16times
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTrials_2_16time.rgb)
                if thisTrials_2_16time != None:
                    for paramName in thisTrials_2_16time:
                        globals()[paramName] = thisTrials_2_16time[paramName]
                
                # --- Prepare to start Routine "BallMoving" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('BallMoving.started', globalClock.getTime())
                Circle_2.setSize((0.2, 0.2))
                Presstoendroutine_2.keys = []
                Presstoendroutine_2.rt = []
                _Presstoendroutine_2_allKeys = []
                sound_2.setSound(frequencyvalue, secs=10, hamming=True)
                sound_2.setVolume(1.0, log=False)
                sound_2.seek(0)
                # Run 'Begin Routine' code from code_5
                final_position = None
                # Run 'Begin Routine' code from code_7
                sound_2.setVolume(0)
                # keep track of which components have finished
                BallMovingComponents = [Circle_2, Wall_2, Target_2, Presstoendroutine_2, sound_2]
                for thisComponent in BallMovingComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "BallMoving" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *Circle_2* updates
                    
                    # if Circle_2 is starting this frame...
                    if Circle_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        Circle_2.frameNStart = frameN  # exact frame index
                        Circle_2.tStart = t  # local t and not account for scr refresh
                        Circle_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(Circle_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Circle_2.started')
                        # update status
                        Circle_2.status = STARTED
                        Circle_2.setAutoDraw(True)
                    
                    # if Circle_2 is active this frame...
                    if Circle_2.status == STARTED:
                        # update params
                        Circle_2.setPos(((extremeLeft-0.1)+t*Speed, 0), log=False)
                    
                    # *Wall_2* updates
                    
                    # if Wall_2 is starting this frame...
                    if Wall_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        Wall_2.frameNStart = frameN  # exact frame index
                        Wall_2.tStart = t  # local t and not account for scr refresh
                        Wall_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(Wall_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Wall_2.started')
                        # update status
                        Wall_2.status = STARTED
                        Wall_2.setAutoDraw(True)
                    
                    # if Wall_2 is active this frame...
                    if Wall_2.status == STARTED:
                        # update params
                        pass
                    
                    # if Wall_2 is stopping this frame...
                    if Wall_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > Wall_2.tStartRefresh + 10-frameTolerance:
                            # keep track of stop time/frame for later
                            Wall_2.tStop = t  # not accounting for scr refresh
                            Wall_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'Wall_2.stopped')
                            # update status
                            Wall_2.status = FINISHED
                            Wall_2.setAutoDraw(False)
                    
                    # *Target_2* updates
                    
                    # if Target_2 is starting this frame...
                    if Target_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        Target_2.frameNStart = frameN  # exact frame index
                        Target_2.tStart = t  # local t and not account for scr refresh
                        Target_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(Target_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Target_2.started')
                        # update status
                        Target_2.status = STARTED
                        Target_2.setAutoDraw(True)
                    
                    # if Target_2 is active this frame...
                    if Target_2.status == STARTED:
                        # update params
                        pass
                    
                    # *Presstoendroutine_2* updates
                    waitOnFlip = False
                    
                    # if Presstoendroutine_2 is starting this frame...
                    if Presstoendroutine_2.status == NOT_STARTED and tThisFlip >= 1/Speed-frameTolerance:
                        # keep track of start time/frame for later
                        Presstoendroutine_2.frameNStart = frameN  # exact frame index
                        Presstoendroutine_2.tStart = t  # local t and not account for scr refresh
                        Presstoendroutine_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(Presstoendroutine_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Presstoendroutine_2.started')
                        # update status
                        Presstoendroutine_2.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(Presstoendroutine_2.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(Presstoendroutine_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if Presstoendroutine_2.status == STARTED and not waitOnFlip:
                        theseKeys = Presstoendroutine_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                        _Presstoendroutine_2_allKeys.extend(theseKeys)
                        if len(_Presstoendroutine_2_allKeys):
                            Presstoendroutine_2.keys = _Presstoendroutine_2_allKeys[-1].name  # just the last key pressed
                            Presstoendroutine_2.rt = _Presstoendroutine_2_allKeys[-1].rt
                            Presstoendroutine_2.duration = _Presstoendroutine_2_allKeys[-1].duration
                            # a response ends the routine
                            continueRoutine = False
                    
                    # if sound_2 is starting this frame...
                    if sound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        sound_2.frameNStart = frameN  # exact frame index
                        sound_2.tStart = t  # local t and not account for scr refresh
                        sound_2.tStartRefresh = tThisFlipGlobal  # on global time
                        # add timestamp to datafile
                        thisExp.addData('sound_2.started', tThisFlipGlobal)
                        # update status
                        sound_2.status = STARTED
                        sound_2.play(when=win)  # sync with win flip
                    
                    # if sound_2 is stopping this frame...
                    if sound_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > sound_2.tStartRefresh + 10-frameTolerance:
                            # keep track of stop time/frame for later
                            sound_2.tStop = t  # not accounting for scr refresh
                            sound_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'sound_2.stopped')
                            # update status
                            sound_2.status = FINISHED
                            sound_2.stop()
                    # update sound_2 status according to whether it's playing
                    if sound_2.isPlaying:
                        sound_2.status = STARTED
                    elif sound_2.isFinished:
                        sound_2.status = FINISHED
                    # Run 'Each Frame' code from code_7
                    if ball.pos[0] > -1.1:
                        sound_2.setVolume(1)
                    else:
                        sound_2.setVolume(0)
                    
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in BallMovingComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "BallMoving" ---
                for thisComponent in BallMovingComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('BallMoving.stopped', globalClock.getTime())
                # check responses
                if Presstoendroutine_2.keys in ['', [], None]:  # No response was made
                    Presstoendroutine_2.keys = None
                trials_2_16times.addData('Presstoendroutine_2.keys',Presstoendroutine_2.keys)
                if Presstoendroutine_2.keys != None:  # we had a response
                    trials_2_16times.addData('Presstoendroutine_2.rt', Presstoendroutine_2.rt)
                    trials_2_16times.addData('Presstoendroutine_2.duration', Presstoendroutine_2.duration)
                sound_2.pause()  # ensure sound has stopped at end of Routine
                # Run 'End Routine' code from code_5
                # Calculate the final position adjusted for the radius
                final_position = (Circle_2.pos[0] - 0.1, Circle_2.pos[1])
                
                # Output the adjusted final position to the data file
                thisExp.addData('final_position_x', final_position[0])
                thisExp.addData('final_position_y', final_position[1])
                # the Routine "BallMoving" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "Rest" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('Rest.started', globalClock.getTime())
                # keep track of which components have finished
                RestComponents = [Wall_3, Target_3]
                for thisComponent in RestComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "Rest" ---
                routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 1.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *Wall_3* updates
                    
                    # if Wall_3 is starting this frame...
                    if Wall_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        Wall_3.frameNStart = frameN  # exact frame index
                        Wall_3.tStart = t  # local t and not account for scr refresh
                        Wall_3.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(Wall_3, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Wall_3.started')
                        # update status
                        Wall_3.status = STARTED
                        Wall_3.setAutoDraw(True)
                    
                    # if Wall_3 is active this frame...
                    if Wall_3.status == STARTED:
                        # update params
                        pass
                    
                    # if Wall_3 is stopping this frame...
                    if Wall_3.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > Wall_3.tStartRefresh + 1-frameTolerance:
                            # keep track of stop time/frame for later
                            Wall_3.tStop = t  # not accounting for scr refresh
                            Wall_3.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'Wall_3.stopped')
                            # update status
                            Wall_3.status = FINISHED
                            Wall_3.setAutoDraw(False)
                    
                    # *Target_3* updates
                    
                    # if Target_3 is starting this frame...
                    if Target_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        Target_3.frameNStart = frameN  # exact frame index
                        Target_3.tStart = t  # local t and not account for scr refresh
                        Target_3.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(Target_3, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Target_3.started')
                        # update status
                        Target_3.status = STARTED
                        Target_3.setAutoDraw(True)
                    
                    # if Target_3 is active this frame...
                    if Target_3.status == STARTED:
                        # update params
                        pass
                    
                    # if Target_3 is stopping this frame...
                    if Target_3.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > Target_3.tStartRefresh + 1-frameTolerance:
                            # keep track of stop time/frame for later
                            Target_3.tStop = t  # not accounting for scr refresh
                            Target_3.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'Target_3.stopped')
                            # update status
                            Target_3.status = FINISHED
                            Target_3.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in RestComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "Rest" ---
                for thisComponent in RestComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('Rest.stopped', globalClock.getTime())
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if routineForceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-1.000000)
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed 2.0 repeats of 'trials_2_16times'
            
            
            # --- Prepare to start Routine "ShortRestwithTarget" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('ShortRestwithTarget.started', globalClock.getTime())
            key_resp_9.keys = []
            key_resp_9.rt = []
            _key_resp_9_allKeys = []
            # Run 'Begin Routine' code from code_4
            current_loop = trials_6times
            
            if trials_6times.thisN == trials_6times.nReps - 1:
                continueRoutine = False
            else:
                continueRoutine = True
            # keep track of which components have finished
            ShortRestwithTargetComponents = [key_resp_9, wall_back_3, StopTarget_3, text_7, aim_3]
            for thisComponent in ShortRestwithTargetComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ShortRestwithTarget" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_9* updates
                waitOnFlip = False
                
                # if key_resp_9 is starting this frame...
                if key_resp_9.status == NOT_STARTED and tThisFlip >= 120-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_9.frameNStart = frameN  # exact frame index
                    key_resp_9.tStart = t  # local t and not account for scr refresh
                    key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_9.started')
                    # update status
                    key_resp_9.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_9.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_9.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_9_allKeys.extend(theseKeys)
                    if len(_key_resp_9_allKeys):
                        key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
                        key_resp_9.rt = _key_resp_9_allKeys[-1].rt
                        key_resp_9.duration = _key_resp_9_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # *wall_back_3* updates
                
                # if wall_back_3 is starting this frame...
                if wall_back_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    wall_back_3.frameNStart = frameN  # exact frame index
                    wall_back_3.tStart = t  # local t and not account for scr refresh
                    wall_back_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(wall_back_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'wall_back_3.started')
                    # update status
                    wall_back_3.status = STARTED
                    wall_back_3.setAutoDraw(True)
                
                # if wall_back_3 is active this frame...
                if wall_back_3.status == STARTED:
                    # update params
                    pass
                
                # *StopTarget_3* updates
                
                # if StopTarget_3 is starting this frame...
                if StopTarget_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    StopTarget_3.frameNStart = frameN  # exact frame index
                    StopTarget_3.tStart = t  # local t and not account for scr refresh
                    StopTarget_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(StopTarget_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'StopTarget_3.started')
                    # update status
                    StopTarget_3.status = STARTED
                    StopTarget_3.setAutoDraw(True)
                
                # if StopTarget_3 is active this frame...
                if StopTarget_3.status == STARTED:
                    # update params
                    pass
                
                # *text_7* updates
                
                # if text_7 is starting this frame...
                if text_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    text_7.frameNStart = frameN  # exact frame index
                    text_7.tStart = t  # local t and not account for scr refresh
                    text_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_7.started')
                    # update status
                    text_7.status = STARTED
                    text_7.setAutoDraw(True)
                
                # if text_7 is active this frame...
                if text_7.status == STARTED:
                    # update params
                    pass
                
                # *aim_3* updates
                
                # if aim_3 is starting this frame...
                if aim_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    aim_3.frameNStart = frameN  # exact frame index
                    aim_3.tStart = t  # local t and not account for scr refresh
                    aim_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(aim_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'aim_3.started')
                    # update status
                    aim_3.status = STARTED
                    aim_3.setAutoDraw(True)
                
                # if aim_3 is active this frame...
                if aim_3.status == STARTED:
                    # update params
                    pass
                # Run 'Each Frame' code from code_4
                keys = key_resp_9.getKeys()
                
                if keys:
                    if keys[0].name == 'space':
                       continueRoutine = False 
                    
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ShortRestwithTargetComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ShortRestwithTarget" ---
            for thisComponent in ShortRestwithTargetComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('ShortRestwithTarget.stopped', globalClock.getTime())
            # check responses
            if key_resp_9.keys in ['', [], None]:  # No response was made
                key_resp_9.keys = None
            trials_6times.addData('key_resp_9.keys',key_resp_9.keys)
            if key_resp_9.keys != None:  # we had a response
                trials_6times.addData('key_resp_9.rt', key_resp_9.rt)
                trials_6times.addData('key_resp_9.duration', key_resp_9.duration)
            # the Routine "ShortRestwithTarget" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 6.0 repeats of 'trials_6times'
        
        
        # --- Prepare to start Routine "SessionBreak" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('SessionBreak.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_2
        current_loop = trials_4sessions
        
        if trials_4sessions.thisN == trials_4sessions.nReps - 1:
            continueRoutine = False
        else:
            continueRoutine = True
        
        key_resp_4.keys = []
        key_resp_4.rt = []
        _key_resp_4_allKeys = []
        # keep track of which components have finished
        SessionBreakComponents = [SessionBreak_2, key_resp_4, Presskey_2]
        for thisComponent in SessionBreakComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "SessionBreak" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *SessionBreak_2* updates
            
            # if SessionBreak_2 is starting this frame...
            if SessionBreak_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                SessionBreak_2.frameNStart = frameN  # exact frame index
                SessionBreak_2.tStart = t  # local t and not account for scr refresh
                SessionBreak_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SessionBreak_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'SessionBreak_2.started')
                # update status
                SessionBreak_2.status = STARTED
                SessionBreak_2.setAutoDraw(True)
            
            # if SessionBreak_2 is active this frame...
            if SessionBreak_2.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from code_2
            keys = key_resp_4.getKeys()
            
            if keys:
                if keys[0].name == 'space':
                   continueRoutine = False 
            
            
            # *key_resp_4* updates
            waitOnFlip = False
            
            # if key_resp_4 is starting this frame...
            if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.tStart = t  # local t and not account for scr refresh
                key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_4.started')
                # update status
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_4.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_4_allKeys.extend(theseKeys)
                if len(_key_resp_4_allKeys):
                    key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                    key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                    key_resp_4.duration = _key_resp_4_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *Presskey_2* updates
            
            # if Presskey_2 is starting this frame...
            if Presskey_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Presskey_2.frameNStart = frameN  # exact frame index
                Presskey_2.tStart = t  # local t and not account for scr refresh
                Presskey_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presskey_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Presskey_2.started')
                # update status
                Presskey_2.status = STARTED
                Presskey_2.setAutoDraw(True)
            
            # if Presskey_2 is active this frame...
            if Presskey_2.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in SessionBreakComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "SessionBreak" ---
        for thisComponent in SessionBreakComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('SessionBreak.stopped', globalClock.getTime())
        # check responses
        if key_resp_4.keys in ['', [], None]:  # No response was made
            key_resp_4.keys = None
        trials_4sessions.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None:  # we had a response
            trials_4sessions.addData('key_resp_4.rt', key_resp_4.rt)
            trials_4sessions.addData('key_resp_4.duration', key_resp_4.duration)
        # the Routine "SessionBreak" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 4.0 repeats of 'trials_4sessions'
    
    
    # --- Prepare to start Routine "SurveyEnd" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('SurveyEnd.started', globalClock.getTime())
    Speeds.reset()
    Strategy.reset()
    Purpose.reset()
    Age.reset()
    Gender.reset()
    # keep track of which components have finished
    SurveyEndComponents = [Survey, Speeds, Strategy, Purpose, Age, Gender, PressCTRL]
    for thisComponent in SurveyEndComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "SurveyEnd" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Survey* updates
        
        # if Survey is starting this frame...
        if Survey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Survey.frameNStart = frameN  # exact frame index
            Survey.tStart = t  # local t and not account for scr refresh
            Survey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Survey, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Survey.started')
            # update status
            Survey.status = STARTED
            Survey.setAutoDraw(True)
        
        # if Survey is active this frame...
        if Survey.status == STARTED:
            # update params
            pass
        
        # *Speeds* updates
        
        # if Speeds is starting this frame...
        if Speeds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Speeds.frameNStart = frameN  # exact frame index
            Speeds.tStart = t  # local t and not account for scr refresh
            Speeds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Speeds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Speeds.started')
            # update status
            Speeds.status = STARTED
            Speeds.setAutoDraw(True)
        
        # if Speeds is active this frame...
        if Speeds.status == STARTED:
            # update params
            pass
        
        # *Strategy* updates
        
        # if Strategy is starting this frame...
        if Strategy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Strategy.frameNStart = frameN  # exact frame index
            Strategy.tStart = t  # local t and not account for scr refresh
            Strategy.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Strategy, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Strategy.started')
            # update status
            Strategy.status = STARTED
            Strategy.setAutoDraw(True)
        
        # if Strategy is active this frame...
        if Strategy.status == STARTED:
            # update params
            pass
        
        # *Purpose* updates
        
        # if Purpose is starting this frame...
        if Purpose.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Purpose.frameNStart = frameN  # exact frame index
            Purpose.tStart = t  # local t and not account for scr refresh
            Purpose.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Purpose, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Purpose.started')
            # update status
            Purpose.status = STARTED
            Purpose.setAutoDraw(True)
        
        # if Purpose is active this frame...
        if Purpose.status == STARTED:
            # update params
            pass
        
        # *Age* updates
        
        # if Age is starting this frame...
        if Age.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Age.frameNStart = frameN  # exact frame index
            Age.tStart = t  # local t and not account for scr refresh
            Age.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Age, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Age.started')
            # update status
            Age.status = STARTED
            Age.setAutoDraw(True)
        
        # if Age is active this frame...
        if Age.status == STARTED:
            # update params
            pass
        
        # *Gender* updates
        
        # if Gender is starting this frame...
        if Gender.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Gender.frameNStart = frameN  # exact frame index
            Gender.tStart = t  # local t and not account for scr refresh
            Gender.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Gender, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Gender.started')
            # update status
            Gender.status = STARTED
            Gender.setAutoDraw(True)
        
        # if Gender is active this frame...
        if Gender.status == STARTED:
            # update params
            pass
        
        # *PressCTRL* updates
        
        # if PressCTRL is starting this frame...
        if PressCTRL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PressCTRL.frameNStart = frameN  # exact frame index
            PressCTRL.tStart = t  # local t and not account for scr refresh
            PressCTRL.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PressCTRL, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PressCTRL.started')
            # update status
            PressCTRL.status = STARTED
            PressCTRL.setAutoDraw(True)
        
        # if PressCTRL is active this frame...
        if PressCTRL.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from code_6
        # In the Each Frame tab of a code component
        
        # Check for keypress events
        keys = event.getKeys()
        
        # Check if 'ctrl' key is pressed
        if 'lctrl' in keys or 'rctrl' in keys:
            # End the routine
            continueRoutine = False
        
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SurveyEndComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "SurveyEnd" ---
    for thisComponent in SurveyEndComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('SurveyEnd.stopped', globalClock.getTime())
    thisExp.addData('Speeds.text',Speeds.text)
    thisExp.addData('Strategy.text',Strategy.text)
    thisExp.addData('Purpose.text',Purpose.text)
    thisExp.addData('Age.text',Age.text)
    thisExp.addData('Gender.text',Gender.text)
    # the Routine "SurveyEnd" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Thank_you" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Thank_you.started', globalClock.getTime())
    # keep track of which components have finished
    Thank_youComponents = [Thankyou]
    for thisComponent in Thank_youComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Thank_you" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Thankyou* updates
        
        # if Thankyou is starting this frame...
        if Thankyou.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Thankyou.frameNStart = frameN  # exact frame index
            Thankyou.tStart = t  # local t and not account for scr refresh
            Thankyou.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Thankyou, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Thankyou.started')
            # update status
            Thankyou.status = STARTED
            Thankyou.setAutoDraw(True)
        
        # if Thankyou is active this frame...
        if Thankyou.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Thank_youComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Thank_you" ---
    for thisComponent in Thank_youComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Thank_you.stopped', globalClock.getTime())
    # the Routine "Thank_you" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
