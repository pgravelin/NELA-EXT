function reset(setAllActive, resetOnly) {
    const defaultFilters = ["title1", "title1_date", "title2", "title2_date", 
        "normal_display", "source1", "source2", "sources_display"];

    $(".field-btn").each(function() {
        const isChecked = $(this).prop("checked");
        const index = defaultFilters.indexOf($(this).prop("id"));

        if ((setAllActive && !isChecked) || (!setAllActive && isChecked && !resetOnly) ||
                (resetOnly && (isChecked && index === -1 && !setAllActive) || 
                (!isChecked && index !== -1))) {
            $(this).trigger("click");
        }
    });
}

function toggleAlert(){
    $(".alert").toggleClass('in out'); 
    return false; // Keep close.bs.alert event from removing from DOM
}

reset(false, true);

/////////////////////////////////////////////////////////////
/** Reset, Select All/Deselect, and Submit button handlers */
/////////////////////////////////////////////////////////////

$("#btn_reset").click(function() {
    reset(false, true);
    toggleAlert();
});

$("#btn_selectall").click(function() {
    const text = $(this).prop("value");
    let selectall = true;

    if (text === "Select all") {
        $(this).prop("value", "Deselect all");
    }
    else {
        $(this).prop("value", "Select all");
        selectall = false;
    }

    reset(selectall, false);
});

$(".field-btn").change(function() {
    const activeButtons = $(".field-btn:checked").length;

    if(activeButtons) { 
        $("#btn_submit1").prop("disabled", false);
    }
    else {
        $("#btn_submit1").prop("disabled", true);
    }
});