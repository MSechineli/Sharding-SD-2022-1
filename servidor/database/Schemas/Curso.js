import mongoose from "mongoose"

const CursoSchema = mongoose.Schema({
  codigo: {
    type: Number,
    require: true
  },
  nome: {
    type: String,
    require: true
  }
})

export default CursoSchema