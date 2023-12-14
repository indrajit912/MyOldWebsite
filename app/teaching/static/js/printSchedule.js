function printTentativeSchedule() {
    // Get the content of the Tentative Schedule table
    var tableContent = document.getElementById("tentativeScheduleTable").outerHTML;

    // Get the styles
    var styles = document.getElementsByTagName('style');
    var styleContent = "";
    for (var i = 0; i < styles.length; i++) {
        styleContent += styles[i].innerHTML;
    }

    // Create a new window for printing
    var printWindow = window.open('', '_blank');

    // Write the styles and table content to the new window
    printWindow.document.write('<html><head><title>Tentative Schedule</title>');
    printWindow.document.write('<style>' + styleContent + '</style>');
    printWindow.document.write('</head><body>');
    printWindow.document.write(tableContent);
    printWindow.document.write('</body></html>');

    // Close the document for printing
    printWindow.document.close();

    // Trigger the print dialog
    printWindow.print();
}