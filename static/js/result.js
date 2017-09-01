/**
 * Created by Administrator on 2017/7/31.
 */
$(function () {

var p;
var u;
var g;
    var main = document.getElementById("main")
    function setOption() {
        var myChart = echarts.init(main);
        var option = [
            /*第一组数据图表*/
            {
                title: {
                    text: '',
                    subtext: ''
                },
                tooltip: { showDelay: 0,
                    hideDelay: 50,
                    transitionDuration:0,
                    backgroundColor : '#27a6ff',
                    borderColor : '#f50',
                    borderRadius : 8,
                    borderWidth: 0,
                    padding: 10,    // [5, 10, 15, 20]
                    position : function(p) {
                        // 位置回调
                        // console.log && console.log(p);
                        return [p[0] + 10, p[1] - 10];},
                    trigger: 'axis', /*显示该点的所有数据*/
                    axisPointer: {
                        type: 'none'//坐标显示器设置为没有
                    },

                },
            
                toolbox: {
                    position:'right',
                 
                    show : true,
                    itemGap: 30,               // 各个item之间的间隔，单位px，默认为10，
                    itemSize:23,
                    feature : {
                        magicType: {
                            show : true,
                            title : {
                               
                                bar : '柱形图',
                            },
                            type : [ 'bar'],
                            color:"#1d2e36"
                        },




                    }


                },
                calculable: true,
                grid: {borderWidth: 0,y:140,
                    width:'93%',




                    /*x:'center'*/
                },//去掉外面的整个矩形边框
                xAxis: [

                    {

                        //设置轴线的属性
                        axisLine: {

                            /*  show: true,*/ // 控制x轴线是否显示
                            lineStyle: {
                                color: '#c8c8c8',
                                width: 1,//这里是为了突出显示加上的
                            }
                        },

                        splitLine: {show: false},//去除网格线
                        axisTick: {
                            show:false,


                        },//去除x轴的刻度线
                        type: 'category',
                        boundaryGap: true,
                        axisLabel: {


                            /* show: true,*/

                            textStyle: {
                                fontSize: 16,
                                color: '#1d2e36'
                            }
                        },
                        data: ['积极态度', '消极态度', '中立态度']
                    }
                ],
                yAxis: [
                    {//去除y轴刻度线
                        axisTick: {
                            show: false
                        },
                        //去除网格线
                        splitLine: {
                            show: true
                        },
                        textStyle: {
                            fontSize: 16,
                            color: '#1d2e36 '},
                        // 控制y轴线是否显示
                        axisLine: {show: false},
                        boundaryGap: false,//不从x轴0刻度开始
                        type: 'value',
                        axisLabel: {
                            formatter: '{value}%'
                        },


                        splitNumber: 4,
                        min: 0,
                        max: 100
                    }
                ],
                series: [
                    /*积极态度*/
                    {
                        smooth: true,
                       
                        type: 'bar',
                      
                        barGap: '100%',//柱形图之间距离
barWidth:100,
                        symbolSize: 4, // 图表的点的大小
                        symbol: 'emptyCircle',//折线点的圆点为空心

                        itemStyle: {
                            normal: {
                                color: '#5197f8',
                                lineStyle: {
                                    color: '#5197f8'
                                }
                            },
                            //鼠标高亮状态
                            emphasis: {
                                label:{
                                    show:false
                                }


                            }
                        },
                        data: [{{p}},{{u}},{{g}}]

                    },
                   

                ]
            },
        ];
        //当屏幕窗口改变时，图表也会发生改变，响应式
        //第一组数据
        window.onresize =function(){
            myChart.resize()

        }
        myChart.setOption(option[0]);
    }
    setOption();
});
