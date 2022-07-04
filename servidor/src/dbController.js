/**
 * Descrição: As funcionalidades de insercao de matricula, alteracao de notas e faltas,
 * listagem de alunos dada uma disciplina e listagem do boletim de um aluno; que se 
 * comunica com o banco de dados, estao sendo gerenciadas neste controller.
 * 
 * @author Matheus Henrique Sechineli
 * @author Vinicius Kuwakino
 * 
 * Data de criação: 27/05/2022
 * Data de atualização: 01/06/2022
 * 
 */

import mongoose from 'mongoose'
import MatriculaSchema from '../database/Schemas/Matricula.js'
import AlunoSchema from '../database/Schemas/Aluno.js'
import DisciplinaSchema from '../database/Schemas/Disciplina.js'

// import { MongoClient } from "mongodb";
// const uri = 'mongodb://localhost:60000';
// const client = new MongoClient(uri);
// async function run(){
//   try {
//     await client.connect();
//     const database = client.db("faculdade");
//     const movies = database.collection("matriculas");
  
//     const cursor = await movies.find({ 
//       cod_disciplina: 'BCC36D',
//       ano: 2022,
//       semestre: 1
//     });
  
//     if ((await cursor.count()) === 0) {
//       console.log("No documents found!");
//     }
//     console.log(cursor)
//   } finally {
//     await client.close();
//   }

// }
// async function run() {
  // try {
  //   await client.connect();
  //   const database = client.db("faculdade");
  //   const movies = database.collection("disciplinas");
  //   // query for movies that have a runtime less than 15 minutes
  //   const cursor = movies.find({ codigo: 'BCC36C' });
  //   // print a message if no documents were found
  //   if ((await cursor.count()) === 0) {
  //     console.log("No documents found!");
  //   }
  //   // replace console.dir with your callback to access individual elements
  //   await cursor.forEach(console.dir);
  // } finally {
  //   await client.close();
  // }
// }
// run().catch(console.dir);

mongoose.Promise = global.Promise
mongoose.connect('mongodb://localhost:60000/faculdade')
  .then(() => {
    console.log('Mongodb conectado...');
  }).catch(() => {
    console.log('Erro ao conectar com o mongo');
  })

  // try {
    
  //   const alunos = await AlunoSchema.findOne({
  //     cod_disciplina: "BCC36C",
  //     ano: 2022,
  //     semestre: 1,
  //   })

  //   console.log(alunos)

  // } catch (error) {
  //   console.log(error);
  // }




/**
 * Funcao do banco de dados que realiza a insercao de matricula.
 * 
 * @param {Request} matricula - recebe os dados da matricula na requisicao do cliente
 * 
 * @returns {Boolean} retorna um boleano da operacao de inserir matricula
 */
export async function dbInsertMatricula(matricula) {
  const { ra, codDisciplina, ano, semestre } = matricula;
  const novaMatricula = {
    ra,
    cod_disciplina: codDisciplina,
    ano,
    semestre,
    nota: 0,
    faltas: 0
  }
  
  try {
    
    const verifyMatricula = await MatriculaSchema.findOne({ 
      ra,
      cod_disciplina: codDisciplina,
      ano,
      semestre
    })

    if (!verifyMatricula) {
      await MatriculaSchema.create(novaMatricula)
      return true;
    }

  } catch (error) {
    console.log(error);
  }
  
  return false;
}


/**
 * Funcao do banco de dados que realiza a atualizacao da nota de uma matricula.
 * 
 * @param {Request} matricula - recebe os dados da matricula na requisicao do cliente
 * 
 * @returns {Boolean} retorna um boleano da operacao de atualizar nota.
 */
export async function dbUpdateNota(matricula) {
  const { ra, codDisciplina, ano, semestre, nota } = matricula;

  try {
    
    const updateNota = await MatriculaSchema.updateOne({
      ra,
      cod_disciplina: codDisciplina,
      ano,
      semestre,
    }, { nota })

    if (updateNota.matchedCount == 1) return true;

  } catch (error) {
    console.log(error);
  }
  
  return false;
}


/**
 * Funcao do banco de dados que realiza a atualizacao das faltas de uma matricula.
 * 
 * @param {Request} matricula - recebe os dados da matricula na requisicao do cliente
 * 
 * @returns {Boolean} retorna um boleano da operacao de atualizar faltas.
 */
export async function dbUpdateFaltas(matricula) {
  const { ra, codDisciplina, ano, semestre, faltas } = matricula;

  try {
    
    const updateFaltas = await MatriculaSchema.updateOne({
      ra,
      cod_disciplina: codDisciplina,
      ano,
      semestre,
    }, { faltas })

    if (updateFaltas.matchedCount == 1) return true;

  } catch (error) {
    console.log(error);
  }
  
  return false;
}


/**
 * Funcao do banco de dados que realiza a listagem de alunos de uma disciplina.
 * 
 * @param {Request} matricula - recebe os dados da matricula na requisicao do cliente
 * 
 * @returns {Array} retorna um array de alunos dada a disciplina.
 */
export async function dbListarAlunos(matricula) {
  const { codDisciplina, ano, semestre } = matricula;
  const arrAlunos = []

  try {
    
    const matriculas = await MatriculaSchema.find({
      cod_disciplina: codDisciplina,
      ano: ano,
      semestre: semestre,
    })
    
    for(const matricula of matriculas) 
      arrAlunos.push(...await AlunoSchema.find({ra: matricula.ra}))

  } catch (error) {
    console.log(error);
  }

  return arrAlunos;
}


/**
 * Funcao do banco de dados que realiza a listagem do boletim dado um aluno.
 * 
 * @param {Request} matricula - recebe os dados da matricula na requisicao do cliente
 * 
 * @returns {Array} retorna um array de disciplinas e matriculas.
 */
export async function dbBoletimAlunos(matricula) {
  const { ra, ano, semestre } = matricula;

  try {
    
    const alunos = await AlunoSchema.find({
      ra: ra,
    })
    
    const matriculas=await MatriculaSchema.find({ano, semestre, ra})

    for(const matricula of matriculas)
      matricula.disciplina = DisciplinaSchema.find({codigo: matricula.cod_disciplina})
    
    console.log(matriculas)
    console.log(alunos)
    return [alunos, matriculas]
  } catch (error) {
    console.log(error);
    throw error
  }

  // const arrMatricula = [];
  // const arrDisciplina = [];

  // const { ra, ano, semestre } = matricula;

  // const statement = await knex('Matricula')
  //   .join('Disciplina', {
  //     'Matricula.cod_disciplina': 'Disciplina.codigo',
  //   })
  //   .where({ ra, ano, semestre });

  // statement.forEach((statement) => {
  //   arrMatricula.push({
  //     ra: statement.ra,
  //     ano: statement.ano,
  //     semestre: statement.semestre,
  //     codDisciplina: statement.cod_disciplina,
  //     faltas: statement.faltas,
  //     nota: statement.nota,
  //   });
  //   arrDisciplina.push({
  //     codigo: statement.codigo,
  //     nome: statement.nome,
  //     professor: statement.professor,
  //     codCurso: statement.cod_curso,
  //   });
  // });

  // return [arrDisciplina, arrMatricula];
}

