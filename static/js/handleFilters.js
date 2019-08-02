$("#btn_submit1").prop("disabled", true);

$("#btn_selectall").click(function() {
    var selectall = true;
    var text = $(this).prop("value");

    if (text === "Select all") {
        $(this).prop("value", "Deselect all");
    }
    else {
        $(this).prop("value", "Select all");
        selectall = false;
    }

    $('.field-btn').each(function() {
        var isChecked = $(this).prop("checked");

        if (!isChecked && selectall) {
            $(this).trigger("click");
        }
        else if (isChecked && !selectall) {
            $(this).trigger("click")
        }
    });
});

$(".field-btn").change(function() {
    var activeButtons = $(".field-btn:checked").length;

    if(activeButtons) { 
        $("#btn_submit1").prop("disabled", false);
    }
    else {
        $("#btn_submit1").prop("disabled", true);
    }
});