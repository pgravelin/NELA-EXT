$('.input-daterange input').each(function() {
    $(this).datepicker('clearDates');
    console.log("K");
});

$('.datepicker').each(function (){
    $(this).datepicker({
        autoclose: true,
        format: 'dd-mm-yyyy',
        todayBtn: "linked"
    });
    console.log("EEK");
});

var sDate,eDate;
$("#start_date").datepicker().on('changeDate',function(e){
    console.log("Start change")
    sDate = new Date($(this).datepicker('getUTCDate'));
    checkDate();
});

$("#end_date").datepicker().on('changeDate',function(date){
    console.log("end change")
    eDate = new Date($(this).datepicker('getUTCDate'));
    checkDate();
});

function checkDate()
{
    if(sDate && eDate && (eDate<sDate))
    {
        
        $("#btn_submit").attr("disabled", true);
    }
    else
    {
        $("#btn_submit").attr("disabled", false);
    }
}