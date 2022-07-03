import mongoose from "mongoose"

const AlunoSchema = mongoose.Schema({
  ra: {
    type: Number,
    require: true
  },
  nome: {
    type: String,
    require: true
  },
  periodo: {
    type: Number,
    require: true
  },
  cod_curso: {
    type: Number,
    require: true
  }
})

export default AlunoSchema