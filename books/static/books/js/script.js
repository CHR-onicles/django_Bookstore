function readMoreFunc() {
  // l_desc and l_desc_trunc are global variables that will be declared at the part of the HTML where the script is included

  var long_desc = document.getElementById("long-desc");
  var btnText = document.getElementById("read-more");

  if (long_desc.innerText.slice(long_desc.innerText.length - 1) === "…") {
    console.log(long_desc.innerText.slice(long_desc.innerText.length - 1));
    long_desc.innerHTML = l_desc;
    btnText.innerHTML = "Read less";
  } else {
    console.log(long_desc.innerText.slice(long_desc.innerText.length - 1));
    btnText.innerHTML = "Read more";
    long_desc.innerText = l_desc_trunc;
  }
}
