function readMore() {
  /**************************
  Document function here
  **************************/
  var long_desc_element = JSON.parse(document.getElementById("long-desc"));
  var long_desc_text = long_desc_element.textContent;
  var btnText = document.getElementById("read-more");

  if (long_desc_text.slice(long_desc_text.length - 1) === "…") {
    console.log(long_desc_text.slice(long_desc_text.length - 1));
    long_desc_text.textContent = 0;
    btnText.innerHTML = "Read less";
  } else {
    console.log(long_desc_text.slice(long_desc_text.length - 1));
    btnText.innerHTML = "Read more";
    long_desc_text.innerText = 0;
  }
}
