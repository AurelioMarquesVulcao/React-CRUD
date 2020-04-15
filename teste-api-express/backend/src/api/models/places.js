const mongoose = require("mongoose");


const placesSchema = mongoose.Schema({
  description: {
    type: String
  },
  price: {
    type: String
  },
  quantity: {
    type: String
  }
});

// onde aponto o cluster

module.exports = mongoose.model("anydata" , placesSchema);
