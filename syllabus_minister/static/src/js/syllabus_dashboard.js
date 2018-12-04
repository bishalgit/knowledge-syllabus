odoo.define('syllabus_minister.dashboard', function (require) {
"use strict";

var core = require('web.core');
var session = require('web.session');
var ajax = require('web.ajax');
var ActionManager = require('web.ActionManager');
var view_registry = require('web.view_registry');
var Widget = require('web.Widget');
var ControlPanelMixin = require('web.ControlPanelMixin');

var QWeb = core.qweb;

var _t = core._t;
var _lt = core._lt;

var SyllabusDashboard = Widget.extend(ControlPanelMixin, {
//	template: 'hr_dashboard.dashboard',
	events: _.extend({}, Widget.prototype.events, {
	    'click .program': 'total_program',
        'click .course': 'total_course',
        'click .faculty': 'total_faculty',
        'click .syllabus': 'total_syllabus',
        // 'click .users': 'total_users',
////        'click .timesheets_to_approve': 'action_timesheets',
////        'click .job_applications': 'action_job_applications',
////        'click .leave_allocations': 'action_leave_allocations',
////        'click .attendance': 'action_attendance',
////        'click .expenses': 'action_expenses',
////        'click #generate_payroll_pdf': function(){this.generate_payroll_pdf("bar");},
//           'click #generate_assignment_pdf': function(){this.generate_assignment_pdf("pie")},
////        'click .my_profile': 'action_my_profile',
	}),
	init: function(parent, context) {
        this._super(parent, context);
        var syllabus_data = [];
        var self = this;
        if (context.tag == 'syllabus_minister.dashboard') {
            self._rpc({
                model: 'syllabus_minister.dashboard',
                method: 'get_syllabus_info',
            }, []).then(function(result){
                self.syllabus_data = result
            }).done(function(){
                self.render();
                console.log(self.syllabus_data);
                self.href = window.location.href;
            });
        }
    },
    willStart: function() {
         return $.when(ajax.loadLibs(this), this._super());
    },
    start: function() {
        var self = this;
        return this._super();
    },
    render: function() {
        var super_render = this._super;
        var self = this;
        var syllabus_dashboard = QWeb.render( 'syllabus_minister.dashboard', {
            widget: self,
        });
        $( ".o_control_panel" ).addClass( "o_hidden" );
        $(syllabus_dashboard).prependTo(self.$el);
        self.graph();
//        self.previewTable();
        return syllabus_dashboard
    },
    reload: function () {
            window.location.href = this.href;
    },
    total_program: function(event) {
        var self = this;
        event.stopPropagation();
        event.preventDefault();
        return this.do_action({
            name: _t("Program"),
            type: 'ir.actions.act_window',
            res_model: 'syllabus_minister.program',
            // src_model: 'hr.employee',
            view_mode: 'tree',
            view_type: 'tree',
            views: [[false, 'list']],
            // context: {'search_default_employee_id': [self.employee_data.id],
            //         'default_employee_id': self.employee_data.id,
            //         'search_default_group_type': true,
            //         'search_default_year': true
            //         },
            // domain: [['holiday_type','=','employee'], ['holiday_status_id.limit', '=', false], ['state','!=', 'refuse']],
            // search_view_id: self.employee_data.leave_search_view_id,
            target: 'current'
        },{on_reverse_breadcrumb: function(){ return self.reload();}})
    },

    total_course: function(event) {
        var self = this;
        event.stopPropagation();
        event.preventDefault();
        return this.do_action({
            name: _t("Course"),
            type: 'ir.actions.act_window',
            res_model: 'syllabus_minister.course',
            // src_model: 'hr.employee',
            view_mode: 'tree',
            view_type: 'tree',
            views: [[false, 'list']],
            // context: {'search_default_employee_id': [self.employee_data.id],
            //         'default_employee_id': self.employee_data.id,
            //         'search_default_group_type': true,
            //         'search_default_year': true
            //         },
            // domain: [['holiday_type','=','employee'], ['holiday_status_id.limit', '=', false], ['state','!=', 'refuse']],
            // search_view_id: self.employee_data.leave_search_view_id,
            target: 'current'
        },{on_reverse_breadcrumb: function(){ return self.reload();}})
    },
    total_faculty: function(event) {
        var self = this;
        event.stopPropagation();
        event.preventDefault();
        return this.do_action({
            name: _t("Faculty"),
            type: 'ir.actions.act_window',
            res_model: 'syllabus_minister.faculty',
            // src_model: 'hr.employee',
            view_mode: 'tree',
            view_type: 'tree',
            views: [[false, 'list']],
            // context: {'search_default_employee_id': [self.employee_data.id],
            //         'default_employee_id': self.employee_data.id,
            //         'search_default_group_type': true,
            //         'search_default_year': true
            //         },
            // domain: [['holiday_type','=','employee'], ['holiday_status_id.limit', '=', false], ['state','!=', 'refuse']],
            // search_view_id: self.employee_data.leave_search_view_id,
            target: 'current'
        },{on_reverse_breadcrumb: function(){ return self.reload();}})
    },
    total_syllabus: function(event) {
        var self = this;
        event.stopPropagation();
        event.preventDefault();
        return this.do_action({
            name: _t("Syllabus"),
            type: 'ir.actions.act_window',
            res_model: 'document.page',
            // src_model: 'hr.employee',
            view_mode: 'tree',
            view_type: 'tree',
            views: [[false, 'list']],
            // context: {'search_default_employee_id': [self.employee_data.id],
            //         'default_employee_id': self.employee_data.id,
            //         'search_default_group_type': true,
            //         'search_default_year': true
            //         },
            // domain: [['holiday_type','=','employee'], ['holiday_status_id.limit', '=', false], ['state','!=', 'refuse']],
            // search_view_id: self.employee_data.leave_search_view_id,
            target: 'current'
        },{on_reverse_breadcrumb: function(){ return self.reload();}})
    },
//     total_users: function(event) {
//         var self = this;
//         event.stopPropagation();
//         event.preventDefault();
//         return this.do_action({
//             name: _t("Users"),
//             type: 'ir.actions.act_window',
//             res_model: 'res.users',
//             // src_model: 'hr.employee',
//             view_mode: 'tree',
//             view_type: 'tree',
//             views: [[false, 'list']],
//             // context: {'search_default_employee_id': [self.employee_data.id],
//             //         'default_employee_id': self.employee_data.id,
//             //         'search_default_group_type': true,
//             //         'search_default_year': true
//             //         },
//             // domain: [['holiday_type','=','employee'], ['holiday_status_id.limit', '=', false], ['state','!=', 'refuse']],
//             // search_view_id: self.employee_data.leave_search_view_id,
//             target: 'current'
//         },{on_reverse_breadcrumb: function(){ return self.reload();}})
// //    // Function which gives random color for charts.
//     },
    // getRandomColor: function () {
    //     var letters = '3456789ABC'.split('');
    //     var color = '#';
    //     for (var i = 0; i < 6; i++ ) {
    //         color += letters[Math.floor(Math.random() * 16)];
    //     }
    //     return color;
    // },
    // Here we are plotting bar,pie chart
    graph: function() {

        var self = this
        var bg_color_list = []
        var ctx1 = this.$el.find('#myChart1')
        var ctx2 = this.$el.find('#myChart2')
        var ctx3 = this.$el.find('#myChart3')
        var ctx4 = this.$el.find('#myChart4')
        // var ctx5 = this.$el.find('#myChart5')

        Chart.plugins.register({
            beforeDraw: function(chartInstance) {
                var ctx1 = chartInstance.chart.ctx;                    
                ctx1.fillStyle = 'white';                   
                ctx1.fillRect(0, 0, chartInstance.chart.width, chartInstance.chart.height);                    
            }
        });

        // for (var i=0;i<=self.syllabus_data.no_faculty;i++){
        //     bg_color_list.push(self.getRandomColor())
        // }


        var data1 = {
            datasets: [{
                label: '# by syllabus',
                data: self.syllabus_data.syllabus_list,
                backgroundColor: self.syllabus_data.random_color_list,
            }],
            // These labels appear in the legend and in the tooltips when hovering different arcs
            labels: self.syllabus_data.faculty_list
        };

        var data2 = {
            datasets: [{
                label: '# by program',
                data: self.syllabus_data.program_list,
                backgroundColor: self.syllabus_data.random_color_list,
            }],
            // These labels appear in the legend and in the tooltips when hovering different arcs
            labels: self.syllabus_data.faculty_list
        };
        
        var data3 = {
            datasets: [{
                label: '# by old version program',
                data: self.syllabus_data.program_old_version_list,
                backgroundColor:self.syllabus_data.random_color_list,
            }],
            // These labels appear in the legend and in the tooltips when hovering different arcs
            labels: self.syllabus_data.program_index
        };
        
        
        var myChart1 = new Chart(ctx1, {
            type: 'bar',
            data: data1,
            options: {
                scales: {
                    yAxes: [{
                    ticks: {
                            beginAtZero: true,
                            userCallback: function(label, index, labels) {
                            // when the floored value is the same as the value we have a whole number
                            if (Math.floor(label) === label) {
                                return label;
                            }
                        },
                    }
                    }]
                }
            }
        });

        var myChart2 = new Chart(ctx2, {
            type: 'bar',
            data: data2,
            options: {
                scales: {
                    yAxes: [{
                    ticks: {
                            beginAtZero: true,
                            userCallback: function(label, index, labels) {
                            // when the floored value is the same as the value we have a whole number
                            if (Math.floor(label) === label) {
                                return label;
                            }
                        },
                    }
                    }]
                }
            }
        });

        // var myChart5 = new Chart(ctx5, {
        //     type: 'bar',
        //     data: data3,
        //     options: {
        //         scales: {
        //             yAxes: [{
        //             ticks: {
        //                     beginAtZero: true,
        //                     userCallback: function(label, index, labels) {
        //                     // when the floored value is the same as the value we have a whole number
        //                     if (Math.floor(label) === label) {
        //                         return label;
        //                     }
        //                 },
        //             }
        //             }]
        //         }
        //     }
        // });

        var option1 = {

        };
        var option2 = {

        };


        var myChart3 = new Chart(ctx3, {
            type: 'pie',
            data: data1,
            options: option1
        });
        
        var myChart4 = new Chart(ctx4, {
            type: 'pie',
            data: data2,
            options: option2
        });
    
        // var lineGraph = new Chart(ctx, {
        //     type: 'line',
        //     data: {
        //         labels: [0,10,20,30,40,50,60],
        //         datasets: [
        //             {
        //                 data: [self.syllabus_data.no_program],
        //                 backgroundColor: "#3e95cd",
        //                 fill: false,
        //             }
        //         ]
        //     },
        //     options: {
        //         title: {
        //           display: true,
        //           text: 'Line graph'
        //         }
        //     }
        // });
    //     for (var i=0;i<=self.assignment_data.studentassignment_len;i++){
    //         bg_color_list.push(self.getRandomColor())
    //     }
    //     var pieChart = new Chart(piectx, {
    //         type: 'pie',
    //         data: {
    //             datasets: [{
    //                 data: [self.assignment_data.pending_len, self.assignment_data.accepted_len, self.assignment_data.denied_len],
    //                 backgroundColor: bg_color_list,
    //                 label: 'Assignment Pie'
    //             }],
    //             labels: ["Pending Assignment", "Completed Assignment", "Denied Assignment"],
    //         },
    //         options: {
    //             responsive: true
    //         }
    //     });

    }

//    generate_assignment_pdf: function(chart) {
//            var canvas = document.querySelector('#assignmentChart');
//        }
//
//        //creates image
//        var canvasImg = canvas.toDataURL("image/jpeg", 1.0);
//        var doc = new jsPDF('landscape');
//        doc.setFontSize(20);
//        doc.addImage(canvasImg, 'JPEG', 10, 10, 280, 150 );
//        doc.save('report.pdf');
//  },
});
core.action_registry.add('syllabus_minister.dashboard', SyllabusDashboard);
return SyllabusDashboard
});