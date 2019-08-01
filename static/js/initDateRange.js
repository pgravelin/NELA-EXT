$(".input-daterange input").each(function() {
    $(this).datepicker("clearDates");
});

$(".datepicker").each(function (){
    $(this).datepicker({
        autoclose: true,
        format: "dd-mm-yyyy",
        todayBtn: "linked"
    });
});

var sDate,eDate;
$("#start_date").datepicker().on("changeDate",function(e){
    sDate = new Date($(this).datepicker("getUTCDate"));
    checkDate();
});

$("#end_date").datepicker().on("changeDate",function(date){
    eDate = new Date($(this).datepicker("getUTCDate"));
    checkDate();
});

function checkDate(){
    if(sDate && eDate && (eDate<sDate)){
        var alert = $('<div class="alert alert-fixed alert-warning alert-dismissable"' +
            '<button type="button" class="close" data-dismiss="alert" aria-hidden="true"></button>' +
            'Danger!!</div>');
        alert.appendTo("#alerts");
        alert.slideDown("slow");

        $("#btn_submit").attr("disabled", true);
    }
    else{
        $("#btn_submit").attr("disabled", false);
    }
}