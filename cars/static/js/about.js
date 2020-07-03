/*
 * @Descripttion: 
 * @version: 
 * @Author: Liang Anqing
 * @Date: 2020-06-29 19:00:11
 * @LastEditors: Liang Anqing
 * @LastEditTime: 2020-06-29 19:03:40
 */ 
function about(){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function (ev) {
        if(xmlHttp.readyState == 4 && xmlHttp.status == 200) {

        }
    }
    xmlHttp.open('GET', 'localhost:5000/about', true)
    xmlHttp.send();
}