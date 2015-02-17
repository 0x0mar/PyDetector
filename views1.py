from django.http import HttpResponse
from django.shortcuts import render_to_response, render
def welcome(request):
    html1=r'''<html>
    <body>hi
    <!-- This Script is from www.htmlfreecodes.com, Provided by: Mahmood Bina -->

    <script>

    // Select fade-effect below:
    // Set 1 if the background may fade from dark to medium
    // Set 2 if the background may fade from light to medium
    // Set 3 if the background may fade from very dark to very light light
    // Set 4 if the background may fade from light to very light
    // Set 5 if the background may fade from dark to very dark
    var fade_effect=3

    // What type of gradient should be applied Internet Explorer 5x or higher?
    // Set "none" or "horizontal" or "vertical"
    var gradient_effect="horizontal"

    // Speed higher=slower
    var speed=60

    ///////////////////////////////////////////////////////////////////////////
    // CONFIGURATION ENDS HERE
    ///////////////////////////////////////////////////////////////////////////

    var browserinfos=navigator.userAgent
    var ie4=document.all&&!document.getElementById
    var ie5=document.all&&document.getElementById&&!browserinfos.match(/Opera/)
    var ns4=document.layers
    var ns6=document.getElementById&&!document.all
    var opera=browserinfos.match(/Opera/)
    var browserok=ie4||ie5||ns4||ns6||opera

    if (fade_effect==1) {
        var darkmax=1
        var lightmax=127
    }
    if (fade_effect==2) {
        var darkmax=127
        var lightmax=254
    }
    if (fade_effect==3) {
        var darkmax=1
        var lightmax=254
    }
    if (fade_effect==4) {
        var darkmax=190
        var lightmax=254
    }
    if (fade_effect==5) {
        var darkmax=1
        var lightmax=80
    }
    var hexc = new Array('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F')

    var newred
    var newgreen
    var newblue
    var oldred
    var oldgreen
    var oldblue

    var redcol_1
    var redcol_2
    var greencol_1
    var greencol_2
    var bluecol_1
    var bluecol_2
    var oldcolor
    var newcolor
    var firsttime=true

    var stepred=1
    var stepgreen=1
    var stepblue=1

    function setrandomcolor() {
        var range=(lightmax-darkmax)
        if (firsttime) {
            newred=Math.ceil(range*Math.random())+darkmax
            newgreen=Math.ceil(range*Math.random())+darkmax
            newblue=Math.ceil(range*Math.random())+darkmax
            firsttime=false
        }

        oldred=Math.ceil(range*Math.random())+darkmax
        oldgreen=Math.ceil(range*Math.random())+darkmax
        oldblue=Math.ceil(range*Math.random())+darkmax

        stepred=newred-oldred
        if (oldred>newred) {stepred=1}
        else if (oldred<newred) {stepred=-1}
        else {stepred=0}

        stepgreen=newgreen-oldgreen
        if (oldgreen>newgreen) {stepgreen=1}
        else if (oldgreen<newgreen) {stepgreen=-1}
        else {stepgreen=0}

        stepblue=newblue-oldblue
        if (oldblue>newblue) {stepblue=1}
        else if (oldblue<newblue) {stepblue=-1}
        else {stepblue=0}
        fadebg()
    }

    function fadebg() {
        if (newred==oldred) {stepred=0}
        if (newgreen==oldgreen) {stepgreen=0}
        if (newblue==oldblue) {stepblue=0}
        newred+=stepred
        newgreen+=stepgreen
        newblue+=stepblue

        if (stepred!=0 || stepgreen!=0 || stepblue!=0) {
            redcol_1 = hexc[Math.floor(newred/16)];
            redcol_2 = hexc[newred%16];
            greencol_1 = hexc[Math.floor(newgreen/16)];
            greencol_2 = hexc[newgreen%16];
            bluecol_1 = hexc[Math.floor(newblue/16)];
            bluecol_2 = hexc[newblue%16];
            newcolor="#"+redcol_1+redcol_2+greencol_1+greencol_2+bluecol_1+bluecol_2
            if (ie5 && gradient_effect!="none") {
                if (gradient_effect=="horizontal") {gradient_effect=1}
                if (gradient_effect=="vertical") {gradient_effect=0}
                greencol_1 = hexc[Math.floor(newred/16)];
                greencol_2 = hexc[newred%16];
                bluecol_1 = hexc[Math.floor(newgreen/16)];
                bluecol_2 = hexc[newgreen%16];
                redcol_1 = hexc[Math.floor(newblue/16)];
                redcol_2 = hexc[newblue%16];
                var newcolorCompl="#"+redcol_1+redcol_2+greencol_1+greencol_2+bluecol_1+bluecol_2
                document.body.style.filter=
    "progid:DXImageTransform.Microsoft.Gradient(startColorstr="+newcolorCompl+", endColorstr="+newcolor+" GradientType="+gradient_effect+")"
            }
            else {
                document.bgColor=newcolor
            }
            var timer=setTimeout("fadebg()",speed);
        }
        else {
            clearTimeout(timer)


    <script>

    // Select fade-effect below:
    // Set 1 if the background may fade from dark to medium
    // Set 2 if the background may fade from light to medium
    // Set 3 if the background may fade from very dark to very light light// Set 4 if the background may fade from light to very light
    // Set 5 if the background may fade from dark to very dark
    var fade_effect=3

    // What type of gradient should be applied Internet Explorer 5x or higher?
    // Set "none" or "horizontal" or "vertical"
    var gradient_effect="horizontal"

    // Speed higher=slower
    var speed=60

    ///////////////////////////////////////////////////////////////////////////
    // CONFIGURATION ENDS HERE
    ///////////////////////////////////////////////////////////////////////////

    var browserinfos=navigator.userAgent
    var ie4=document.all&&!document.getElementById
    var ie5=document.all&&document.getElementById&&!browserinfos.match(/Opera/)
    var ns4=document.layers
    var ns6=document.getElementById&&!document.all
    var opera=browserinfos.match(/Opera/)
    var browserok=ie4||ie5||ns4||ns6||opera

    if (fade_effect==1) {
            var darkmax=1
            var lightmax=127
    }
    if (fade_effect==2) {
            var darkmax=127
            newred=oldred
            newgreen=oldgreen
            newblue=oldblue
            oldcolor=newcolor
            setrandomcolor()
        }
    }

    if (browserok) {
        window.onload=setrandomcolor
    }
    </script></body></html>'''
    #return HttpResponse(html1)
    return  render(request, 'logs.html')


