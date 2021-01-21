import elsie

slides = elsie.Slides()

MAJOR_COLOR = "#86c800"
MINOR_COLOR = "#d2d9bd"

slides.update_style("default", elsie.TextStyle(color="#86b800"))
slides.update_style("alert", elsie.TextStyle(color="#c87600", bold=True))


TITLE_STYLE = elsie.TextStyle(size=32, align="right", color="white")

def slide_with_title(root, text):
    root.sbox(height=80).rect(bg_color=MAJOR_COLOR).fbox(p_right=40).text(text, TITLE_STYLE)
    return root.fbox()


@slides.slide()
def intro(slide):
    head_style = elsie.TextStyle(size=35)
    slide.box().text("State-Space Reduction of Non-deterministically\n"
                     "Synchronizing Systems Applicable to\n"
                     "Deadlock Detection in MPI", head_style)

    slide.box(height=40)
    slide.box().text("Stanislav Böhm¹, Ondřej Meca¹, Petr Jančar²")
    slide.box(height=40)
    slide.box().text("¹ IT4Innovations - National Supercomputing Center, Czech Republic\n"
               "² FEI, Technical University of Ostrava, Czech Republic", elsie.TextStyle(size=18))


@slides.slide()
def hpc(slide):
    slide.image("imgs/hpc.svg", scale=0.9)


@slides.slide()
def mpi(slide):
    slide = slide_with_title(slide, "MPI - Message Passing Interface")
    slide.set_style("emph", elsie.TextStyle(bold=True))
    slide.box(height="70%").rect(bg_color="#eee").box(p_x=30, p_y=15).code("c",
"""~emph{MPI_Init}(&argc, &argv);
int rank;
~emph{MPI_Comm_rank}(MPI_COMM_WORLD, &rank);
int size;
~emph{MPI_Comm_size}(MPI_COMM_WORLD, &size);
int value;
if (rank == 0) {
    value = 0;
    ~emph{MPI_Send}(&value, 1, MPI_INT,
            (rank + 1) % size,
            0, MPI_COMM_WORLD);
}
for (int t=0; t < 1000; t++) {
    ~emph{MPI_Recv}(&value, 1, MPI_INT,
                MPI_ANY_SOURCE,
                MPI_ANY_TAG,
                MPI_COMM_WORLD,
                MPI_STATUS_IGNORE);

    ~emph{MPI_Send}(&value, 1, MPI_INT,
                (rank + 1) % size,
                0, MPI_COMM_WORLD);
}
~emph{MPI_Finalize}();""", scale_to_fit=True, use_styles=True)


@slides.slide()
def highlight_title1(slide):
    slide.text("State-Space Reduction of Non-deterministically\n"
                "Synchronizing Systems Applicable to\n"
                "Deadlock Detection in ~alert{MPI}")


@slides.slide()
def highlight_title2(slide):
    slide.text("State-Space Reduction of ~alert{Non-deterministically\n"
                "Synchronizing Systems} Applicable to\n"
                "Deadlock Detection in ~alert{MPI}")

@slides.slide()
def sends(slide):
    slide.image("imgs/sends.svg")


@slides.slide()
def example(slide):
    slide.image("imgs/example.svg")


@slides.slide()
def approach(slide):
    slide.image("imgs/approach.svg")


@slides.slide()
def observation(slide):
    slide = slide_with_title(slide, "Observation")
    slide.text("Choices inside MPI_Sends: no new behavior (except deadlocks)")



@slides.slide()
def new_approach2(slide):
    slide = slide_with_title(slide, "New approach")
    slide.box().text("(1) Build a state space while considering\n"
                     "      only ~emph{eager} MPI_Send\n\n\n"
                     "(2) Find missing deadlocks", elsie.TextStyle(align="left"))


@slides.slide()
def new_approach(slide):
    slide = slide_with_title(slide, "New approach")
    slide.image("imgs/sspace.svg", scale=0.8)



@slides.slide()
def new_approach3c(slide):
    slide = slide_with_title(slide, "Approach 3")
    slide.box().text("(1) Build a ~alert{parial-order reduced} state space while considering\n"
                     "      only ~emph{eager} MPI_Send\n\n\n"
                     "(2) Find missing deadlocks", elsie.TextStyle(align="left"))


@slides.slide()
def approach3(slide):
    slide = slide_with_title(slide, "Approach 3")
    slide.image("imgs/sspace2.svg", scale=0.8)


@slides.slide()
def problem(slide):
    s = elsie.TextStyle(align="left", size=22)
    slide = slide_with_title(slide, "Problem")
    slide.box(p_bottom=20).text("~alert{Input}")
    slide.box().text("~alert{R} - a system obtained by applying any* POR method on a system ~alert{T}\n"
              "any POR that preserves Mazurkiewicz Traces\n"
              "~alert{I} - the independent set used in reduction\n"
              "~alert{C} - set of 'candidates' that may nondetermistically synchronize", s)
    slide.box(height=60)
    slide.box(p_bottom=20).text("~alert{Output}")
    slide.box().text("Is there a deadlock in ~alert{T} while considering synchronizations of ~alert{C} ?", s)


@slides.slide()
def aislinn(slide):
    slide = slide_with_title(slide, "Aislinn")
    slide.box().text("http://verif.cs.vsb.cz/aislinn/")
    slide.box().image("imgs/aislinn.svg", scale=0.7)


@slides.slide()
def speedup(slide):
    slide = slide_with_title(slide, "Aislinn")
    slide.box().text("Approach 3 compared to Approach 2 (with optimizations)")
    slide.box().text("~alert{3x - 15x} speedup")


slides.render("slides.pdf")
