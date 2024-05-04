package project.resapi.EntidadesRest;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.annotation.Id;

@Data//para getters y setters
@AllArgsConstructor// Construir constructor
@NoArgsConstructor// constructor vacio
@Document(collection = "Courses")//definiendo como documento(entidad)

public class Cursos {
    @Id
    private String _id;
    private String name;
    private String category;
    private Double price;
    private Integer totalHours;
    private boolean certification;
    private Integer id_course;
}

