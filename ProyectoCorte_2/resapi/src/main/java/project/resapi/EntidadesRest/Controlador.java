package project.resapi.EntidadesRest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

@RestController
@RequestMapping("/api")

public class Controlador {
    @Autowired

    private CursosServiceIMPL psimpl;

    @GetMapping("/allCourses")
    public ResponseEntity<Flux<Cursos>> allCourses(){
        Flux<Cursos> flux=this.psimpl.allCourses();
        return new ResponseEntity<Flux<Cursos>>(flux, HttpStatus.OK);
    }

    @PostMapping("/addCourses") //para enviar datos crearlos
    public ResponseEntity<Mono<Cursos>> addCourses(@RequestBody Cursos cursos){
        Mono<Cursos> cursosMono=this.psimpl.addCourses(cursos);
        return new ResponseEntity<Mono<Cursos>>(cursosMono, HttpStatus.CREATED);
    }

    @PutMapping("/updateCourses") //para actualizar
    public ResponseEntity<Mono<Cursos>> updateCourses(@RequestBody Cursos cursos){
        Mono<Cursos> cursosMono=this.psimpl.updateCourses(cursos);
        return new ResponseEntity<Mono<Cursos>>(cursosMono, HttpStatus.CREATED);
    }


    @GetMapping("/findCourses{_id}") //obtener resultado
    public ResponseEntity<Mono<Cursos>> findCourses(@PathVariable String _id){
        Mono<Cursos> cursosMono=this.psimpl.findCourses(_id);
        return new ResponseEntity<Mono<Cursos>>(cursosMono, HttpStatus.OK);
    }


    @DeleteMapping("/deleteCourses{_id}") //para enviar datos crearlos
    public ResponseEntity<Mono<Void>> deleteCourses(@PathVariable String _id){
        Mono<Void> cursosMono=this.psimpl.deleteCourses(_id);
        return new ResponseEntity<Mono<Void>>(cursosMono, HttpStatus.CREATED);
    }

    @DeleteMapping("/deleteAllCourses") //para enviar datos crearlos
    public ResponseEntity<Mono<Void>> deleteAllCourses(){
        Mono<Void> cursosMono=this.psimpl.deleteAllCourses();
        return new ResponseEntity<Mono<Void>>(cursosMono, HttpStatus.CREATED);
    }






}
