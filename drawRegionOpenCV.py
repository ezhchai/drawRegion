#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
drawRegion.py
Draw a ROI region by click the left button of the mouse.
'''

import numpy as np
import cv2 as cv


def on_mouse(event, x, y, flags, param):
    '''
    Callback function to respond the mouse left button down action
    Args:
        event:  mouse event code
        x:      image col index of the mouse point location
        y:      image col index of the mouse point location
    '''
    if event == cv.EVENT_LBUTTONDOWN:
        '''respond the left button click action'''
        ptls.append([x, y])
        cmimg = cmsrc.copy()
        cmmask = np.zeros((cmW, cmH), np.uint8)
        if len(ptls) > 1:
            for i in range(len(ptls)-1):
                # draw lines if the number of clicked points lager than 1
                cv.line(cmimg, tuple(ptls[i]), tuple(ptls[i+1]), green, 5)
            if len(ptls) > 2:
                # draw polygon if the number of clicked points lager than 2
                cv.polylines(cmimg, np.array([ptls], np.int32), True, black, 3)
                cv.fillPoly(cmmask, np.array([ptls], np.int32), white, 1)
                '''draw the polygon by the clicked point of the image'''
                image, contours, hierarchy = cv.findContours(cmmask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
                cv.drawContours(cmmask, contours, -1, white, -1)
                cv.drawContours(cmimg, contours, -1, white, 1)
                '''
                Find the extreme outer contours of the polygon to fill the overlap holes.
                Comment the upper 3 lines if you want to show the overlap holes.
                '''
                cmdst = cv.bitwise_and(cmsrc, cmsrc, mask=cmmask)
                cv.imshow('dst', cmdst)
                cv.imshow('mask', cmmask)
            cv.imshow('src', cmimg)
            cv.waitKey(0)


if __name__ == '__main__':
    ptls = []
    green = (0, 255, 0)
    black = (0, 0, 0)
    white = (255, 255, 255)
    '''define the line colors'''
    cmsrc = cv.imread('lena.jpg')
    cmW, cmH, cmC = cmsrc.shape
    cmimg = cmsrc.copy()
    '''load the image'''
    cv.imshow('src', cmimg)
    cv.setMouseCallback('src', on_mouse)
    '''show image and set the callback function'''
    cv.waitKey(0)

    cv.destoryAllWindows()
