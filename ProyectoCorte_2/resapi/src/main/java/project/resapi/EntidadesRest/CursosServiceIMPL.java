package project.resapi.EntidadesRest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

@Service
public class CursosServiceIMPL {
    @Autowired
    private CursosRepo repo;

    public Flux<Cursos> allCourses(){ //metodo para enviar u obtener varios datos
        
        return this.repo.findAll();
    }
    public Mono<Cursos> addCourses(Cursos cursos){ //metodo para enviar y obtener un dato
        return this.repo.save(cursos);
    }


    public Mono<Cursos> updateCourses(Cursos cursos){ //metodo para actualizar
        return this.repo.save(cursos);
    }
    public Mono<Cursos> findCourses(String _id){ //metodo para buscar por id_course
        return this.repo.findById(_id);
    }
    public Mono<Void> deleteCourses(String _id){ //metodo para eliminar y definilor como vacio
        return this.repo.deleteById(_id);
    }
    public Mono<Void> deleteAllCourses(){ //metodo para eliminar varios y definirlo como vacio
        return this.repo.deleteAll();
    }
}
