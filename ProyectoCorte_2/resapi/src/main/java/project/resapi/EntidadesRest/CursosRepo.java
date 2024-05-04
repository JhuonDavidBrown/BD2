package project.resapi.EntidadesRest;
import org.springframework.data.mongodb.repository.ReactiveMongoRepository;
import org.springframework.stereotype.Repository;


@Repository //definirla como repositorio
public interface CursosRepo extends ReactiveMongoRepository<Cursos,String>{

}
