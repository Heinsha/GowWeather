###
if len(forecast1str) > 120:
        offset1 = 195
        str1 = "true"
else:
        offset1 = 185
        str1 = "false"
###
if len(forecast2str) > 120 and str1 is "true":
        offset2 = 235
        str2 = "truee"
elif len(forecast2str) > 120 or str1 is "true":
        offset2 = 225
        str2 = "true"
elif len(forecast2str) > 120 and str1 is "false":
        offset2 = 215
        str2 = "true"
else:
        offset2 = 205
        str2 = "false"
###
if len(forecast3str) > 120 and str1 is "true" and str2 is "truee":
        offset3 = 265
elif len(forecast3str) > 120 and str1 is "true" and str2 is "true":
        offset3 = 255
elif len(forecast3str) > 120 and str1 is "false" and str2 is "true":
        offset3 = 235
elif len(forecast3str) > 120 and str1 is "true" and str2 is "false":
        offset3 = 235
else:
        offset3 = 225