/**
 * Created by Administrator on 2017/7/31.
 */
$(function () {
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
                legend: {
                    y:90,
                    data: ['pos', 'neg', '其他'],
                    itemGap: 100,               // 各个item之间的间隔，单位px，默认为10，
                    itemWidth: 17,            // 图例图形宽度
                    itemHeight: 15,            // 图例图形高度*/
                },
                toolbox: {
                    position:'right',
                    featureImageIcon:{
                        line : {icon:"images/line-sel.png",
                            bar :{icon:"images/pillar-sel.png"}
                        },
                    },
                    show : true,
                    itemGap: 30,               // 各个item之间的间隔，单位px，默认为10，
                    itemSize:23,
                    feature : {
                        magicType: {
                            show : true,
                            title : {
                                line : '折线图',
                                bar : '柱形图',
                            },
                            type : ['line', 'bar'],
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
                        data: [ '1', '2', '3', '4', '5', '6']
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
                            formatter: '{value} %'
                        },


                        splitNumber: 4,
                        min: 0,
                        max: 100
                    }
                ],
                series: [
                    /*入管温度*/
                    {
                        smooth: true,
                        name: 'pos',
                        type: 'line',
                        barCategoryGap: '50%',//柱形图之间距离
                        barGap: 5,//柱形图之间距离
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
                        data: [12,20,90,89,13,56]

                    },
                    /*出管温度*/
                    {
                        smooth: true,
                        name: 'neg',
                        type: 'line',
                        barCategoryGap: '50%',//柱形图之间距离
                        barGap: 5,//柱形图之间距离
                        symbolSize: 4, // 图表的点的大小
                        symbol: 'emptyCircle',//折线点的圆点为空心
                        itemStyle: {
                            normal: {
                                color: '#ffc869',
                                lineStyle: {
                                    color: '#ffc869'
                                }
                            },
                            emphasis: {
                                label: {
                                    show: false,
                                    color: '#5298f8'
                                }

                            }
                        },
                        data: [15,60,10,57,83,66]

                    },
                    /*COT温度还不知道，随便编的*/
                    {
                        smooth: true,
                        name: '其他',
                        type: 'line',
                        barCategoryGap: '50%',//柱形图之间距离
                        barGap: 5,//柱形图之间距离
                        symbolSize: 4, // 图表的点的大小
                        symbol: 'emptyCircle',//折线点的圆点为空心
                        itemStyle: {
                            normal: {
                                color: '#ff696a',//折线点的颜色
                                lineStyle: {
                                    color: '#ff696a'//折线颜色
                                }
                            }
                        },
                        data: [12,20,90,89,13,56]

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