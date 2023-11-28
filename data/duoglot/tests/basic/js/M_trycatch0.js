try {
  throw Error("CustomError");
} catch (e) {
  console.log("Exception!");
  console.log(e);
} 
  