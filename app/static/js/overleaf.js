// app/static/js/overleaf.js

// This function creates the "Open in Overleaf" functionality.
function openOverleaf(snipUri) {
    // Create a form element
    var form = document.createElement('form');
    form.action = 'https://www.overleaf.com/docs';
    form.method = 'post';
    form.target = '_blank';

    // Create an input element for the snip_uri
    var input = document.createElement('input');
    input.type = 'text';
    input.name = 'snip_uri';
    input.value = snipUri;

    // Append the input to the form
    form.appendChild(input);

    // Append the form to the body and submit it
    document.body.appendChild(form);
    form.submit();

    // Remove the form from the body
    document.body.removeChild(form);
}
