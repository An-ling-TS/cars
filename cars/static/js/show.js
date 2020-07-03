/*
 * @Descripttion: 
 * @version: 
 * @Author: Liang Anqing
 * @Date: 2020-06-30 23:27:22
 * @LastEditors: Liang Anqing
 * @LastEditTime: 2020-07-03 12:21:33
 */ 
var chart_1 
var chart_2 
var chart_3
var chart_4 
var chart_5 
$.ajax({  
    type: "GET",  
    url:"/getcitymax",  
    //data:$('#cars').serialize(),  
    async: true,
    beforeSend:function(){
        //loading()
    },
    error: function(request) {  
        //alert("Connection error");  
    },  
    success: function(data) {  
        //接收后台返回的结果
        
        var rep=data
        var citys = [];
        var values = [];
        for(var i = 0; i < rep.length; i++) {
            citys.push(rep[i].city);
            values.push(rep[i].max);
        }

        chart_2 = echarts.init($("#div-2").get(0),'dark');
        var option = {

            title: {
                text: '城市最高成交额'
            },
            tooltip: {
                trigger: 'axis',//坐标轴触发，主要在柱状图，折线图等会使用类目轴的图表中使用。
                formatter : '{a}</br>城市代码:{b}</br>成交额:{c}'
            },
            grid:{
                left:'2%',
                containLabel: true
            },
            legend: {
                data: ["成交额"]
            },
            xAxis: {
                data: citys
            },
            toolbox: {
                feature: {
                    magicType: {
                        type: ['line', 'bar']
                    },
                    dataView: {},
                }
            },
            yAxis: {left:20},
            series: [{
                left:200,
                name: '成交额',
                type: 'line',
                data: values,
                animationDelay: function (idx) {
                    return idx * 10;
                }
            }],
            animationEasing: 'elasticOut',
            animationDelayUpdate: function (idx) {
                return idx * 5;
            }
        }
        chart_2.setOption(option)
    }  
});
$.ajax({  
    type: "GET",  
    url:"/getcityaverage",  
    //data:$('#cars').serialize(),  
    async: true,
    beforeSend:function(){
        //loading()
    },
    error: function(request) {  
        //alert("Connection error");  
    },  
    success: function(data) {  
        //接收后台返回的结果
        
        var rep=data
        var citys = [];
        var values = [];
        for(var i = 0; i < rep.length; i++) {
            citys.push(rep[i].city);
            values.push(rep[i].average);
        }

        chart_4 = echarts.init(document.getElementById("div-4"),'dark');
        var option = {

            title: {
                text: '城市最高成交额'
            },
            tooltip: {
                trigger: 'axis',//坐标轴触发，主要在柱状图，折线图等会使用类目轴的图表中使用。
                formatter : '{a}</br>城市代码:{b}</br>成交额:{c}'
            },
            legend: {
                data: ["成交额"]
            },
            xAxis: {
                data: citys
            },
            toolbox: {
                feature: {
                    magicType: {
                        type: ['line', 'bar']
                    },
                    dataView: {},
                }
            },
            yAxis: {left:20},
            series: [{
                left:200,
                name: '成交额',
                type: 'line',
                data: values,
                animationDelay: function (idx) {
                    return idx * 10;
                }
            }],
            animationEasing: 'elasticOut',
            animationDelayUpdate: function (idx) {
                return idx * 5;
            }
        }
        chart_4.setOption(option)
    }  
});
$.ajax({  
    type: "GET",  
    url:"/getcitysum",  
    //data:$('#cars').serialize(),  
    async: true,
    beforeSend:function(){
        //loading()
    },
    error: function(request) {  
        //alert("Connection error");  
    },  
    success: function(data) {  
        //接收后台返回的结果
        
        var rep=data
        var datas=[]
        for(var i = 0; i < rep.length; i++) {
            var data={
                name:'',
                value:''
            }
            data.name=rep[i].city;
            data.value=rep[i].sum;
            datas.push(data)
        }

        chart_3 = echarts.init(document.getElementById("div-3"),'dark');
        var option = {

            title: {
                text: '各城市合计成交额'
            },
            tooltip: {
                trigger: 'item',//坐标轴触发，主要在柱状图，折线图等会使用类目轴的图表中使用。
                formatter : '{a}</br>城市代码:{b}</br>成交额:{c}</br>({d}%)'
            },
            
            series: [{
                left:200,
                name: '成交额',
                type: 'pie',
                data: datas,
                animationDelay: function (idx) {
                    return idx * 10;
                }
            }],
            animationEasing: 'elasticOut',
            animationDelayUpdate: function (idx) {
                return idx * 5;
            }
        }
        chart_3.setOption(option)
    }  
});

function load_model(dom){
    var kind='';
    $("#div-1").html()
    //alert(typeof(dom))
    if(typeof(dom)=="string")
        kind=dom
    else
        kind=dom.innerText
    var path='/getmodel'+kind
    $.ajax({  
        type: "GET",  
        url:path,  
        //data:$('#cars').serialize(),  
        async: true,
        beforeSend:function(){
            //loading()
        },
        error: function(request) {  
            //alert("Connection error");  
        },  
        success: function(data) {  
            
            //接收后台返回的结果
            var rep=data
            var texts=""
            var models = [];
            var values = [];
            for(var i = 0; i < rep.length; i++) {
                models.push(rep[i].model);
                if(kind=='max'){
                    values.push(rep[i].max);
                    texts="车型最大成交额"
                }   
                if(kind=='average'){
                    values.push(rep[i].average);
                    texts= "车型平均成交额"
                }
                if(kind=='sum'){
                    values.push(rep[i].sum);
                    texts="车型合计成交额"
                }
            }
            chart_1 = echarts.init(document.getElementById("div-1"),'dark');
            var option = {
                
                title: {
                    text: texts
                },
                tooltip: {
                    trigger: 'axis',//坐标轴触发，主要在柱状图，折线图等会使用类目轴的图表中使用。
                    formatter : '{a}</br>车型代码:{b}</br>成交额:{c}'
                },
                legend: {
                    data: ["成交额"]
                },
                xAxis: {
                    data: models
                },
                toolbox: {
                    feature: {
                        magicType: {
                            type: ['line', 'bar']
                        },
                        dataView: {},
                    }
                },
                grid:{
                    left:'2%',
                    containLabel: true
                },
                yAxis: {left:0},
                series: [{
                    left:-200,
                    name: '成交额',
                    type: 'bar',
                    data: values,
                    animationDelay: function (idx) {
                        return idx * 10;
                    }
                }],
                animationEasing: 'elasticOut',
                animationDelayUpdate: function (idx) {
                    return idx * 5;
                }
            }
            chart_1.setOption(option)
        }  
    });
}
load_model('average')
function load_brand(dom){
    var kind='';
    $("#div-5").html()
    //alert(typeof(dom))
    if(typeof(dom)=="string")
        kind=dom
    else
        kind=dom.innerText
    var path='/getbrand'+kind
    $.ajax({  
        type: "GET",  
        url:path,  
        //data:$('#cars').serialize(),  
        async: true,
        beforeSend:function(){
            //loading()
        },
        error: function(request) {  
            //alert("Connection error");  
        },  
        success: function(data) {  
            
            //接收后台返回的结果
            var rep=data
            var texts=""
            var brands = [];
            var values = [];
            for(var i = 0; i < rep.length; i++) {
                brands.push(rep[i].brand);
                if(kind=='max'){
                    values.push(rep[i].max);
                    texts="品牌最大成交额"
                }   
                if(kind=='average'){
                    values.push(rep[i].average);
                    texts= "品牌平均成交额"
                }
            }
            var chart = null;

            if (chart && chart.dispose) {
                chart.dispose();
            }
            chart_5 = echarts.init(document.getElementById("div-5"),'dark');
            var option = {
                
                title: {
                    text: texts,
        
                },
                tooltip: {
                    trigger: 'axis',//坐标轴触发，主要在柱状图，折线图等会使用类目轴的图表中使用。
                    formatter : '{a}</br>品牌代码:{b}</br>成交额:{c}'
                },
                legend: {
                    data: ["成交额"]
                },
                xAxis: {
                    data: brands
                },
                toolbox: {
                    feature: {
                        magicType: {
                            type: ['line', 'bar']
                        },
                        dataView: {},
                    }
                },
                grid:{
                    left:'2%',
                    containLabel: true
                },
                yAxis: {left:0},
                series: [{
                    left:-200,
                    name: '成交额',
                    type: 'bar',
                    data: values,
                    animationDelay: function (idx) {
                        return idx * 10;
                    }
                }],
                animationEasing: 'elasticOut',
                animationDelayUpdate: function (idx) {
                    return idx * 5;
                }
            }
            chart_5.setOption(option)
        }  
    });
}
function load_brand_sum(){
    $("#div-5").html()
    $.ajax({  
        type: "GET",  
        url:"/getbrandsum",  
        //data:$('#cars').serialize(),  
        async: true,
        beforeSend:function(){
            //loading()
        },
        error: function(request) {  
            //alert("Connection error");  
        },  
        success: function(data) {  
            
            //接收后台返回的结果
            var rep=data
            var texts="各品牌成交额"
            var datas = [];
            
            for(var i = 0; i < rep.length; i++) {
                var data={
                    name:'',
                    value:''
                }
                data.name=rep[i].brand;
                data.value=rep[i].sum;
                datas.push(data)
            }
            var chart = null;

            if (chart && chart.dispose) {
                chart.dispose();
            }
            chart_5 = echarts.init(document.getElementById("div-5"),'dark');
            var option = {
                
                title: {
                    text: texts
                },
                tooltip: {
                    trigger: 'item',//坐标轴触发，主要在柱状图，折线图等会使用类目轴的图表中使用。
                    formatter : '{a}</br>品牌代码:{b}</br>成交额:{c}</br>({d}%)'
                },

                series: [{
                    left:-200,
                    name: '成交额',
                    type: 'pie',
                    radius: [0, '70%'],
                    label: {
                        position: 'inner'
                    },
                    labelLine: {
                        show: false
                    },
                    data: datas,
                    animationDelay: function (idx) {
                        return idx * 10;
                    }
                }],
                animationEasing: 'elasticOut',
                animationDelayUpdate: function (idx) {
                    return idx * 5;
                }
            }
            chart_5.setOption(option)
        }  
    });
}
load_brand('max')
 
window.addEventListener("resize",function (){
    //alert()
    chart_1.resize();
    chart_2.resize();
    chart_3.resize();
    chart_4.resize();
    chart_5.resize();
});