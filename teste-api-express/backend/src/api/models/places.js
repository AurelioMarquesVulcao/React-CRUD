const mongoose = require("mongoose");


const placesSchema = mongoose.Schema({
  name: {
    type: String
  },
  email: {
    type: String
  }
});

// onde aponto o cluster

module.exports = mongoose.model("anydata" , placesSchema);
