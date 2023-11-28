function get_content(line_mode) {
  let f = fs.open('test.txt', 'r');
  if(!line_mode) {
    let ret_value = fs.read(f);
    fs.close(f);
    return ret_value;
  } else {
    let ret_value = fs.read(f).split("\n");
    fs.close(f);
    return ret_value;
  }
}