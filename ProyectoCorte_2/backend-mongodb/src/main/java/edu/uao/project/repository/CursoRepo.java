
package edu.uao.project.repository;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import edu.uao.project.model.Curso;

@Repository //definirla como repositorio
public interface CursoRepo extends MongoRepository<Curso,String>{

}
