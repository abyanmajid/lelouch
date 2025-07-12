prompt_domain = """- Classic DSA Problems (logic bugs, bounds, types)
  - Palindrome check
  - Binary search, linear search
  - Sorting algorithms (bubble, merge, quick)
  - Recursion-based problems (factorial, Fibonacci)
  - Tree traversal, linked list manipulation
  - HashMap vs Array handling
  - Graph problems (DFS, BFS)
  - Matrix rotation, pathfinding

- 📚 CS Education / Assignments
  - Calculator CLI
  - Unit converter
  - Student record manager
  - Grade average calculator
  - Simple compiler/tokenizer/parser

- 🏢 Business / Enterprise Logic
  - Bank account / transaction service
  - User authentication system
  - Bookstore inventory management
  - Invoice generator
  - File importer/parser (CSV, XML, JSON)
  - Config loader
  - REST API mockup
  - Data transfer object (DTO) mapper

- 🧰 Utility Classes
  - Date formatter
  - String normalizer
  - File renamer
  - CSV exporter
  - JSON serializer

- 🌐 Web-related Java Code
  - HTTP request builder
  - Cookie/session manager
  - Web scraper using Jsoup
  - Simple servlet / controller

- ⚙️ Concurrency & Threads
  - Producer-consumer
  - Thread pool misuse
  - Synchronized blocks
  - Race condition simulators
  - Deadlock-prone code

- 🧪 Testing & Mocking
  - Test suite with no assertions
  - Mockito misuse
  - Unmockable static methods
  - Integration test with hardcoded data

- 🔒 Security-related Examples
  - SQL injection prone method
  - Password stored in plaintext
  - Logger printing PII
  - Unvalidated user input

- 🧩 Design Patterns
  - Factory pattern misuse
  - Singleton with shared state
  - Observer with memory leak
  - Incorrect abstraction in Adapter

- 💬 Chatbots / CLI Interaction
  - Menu-driven CLI app
  - Quiz app
  - Command interpreter

- 🛠 Java 8+ Features
  - Misuse of streams
  - Unnecessary Optional.get()
  - Lambda expressions with side effects
  - Collectors.toMap() collision bug
"""

formatting_rules = """2. Vary across:
   - Variable/class/method naming (e.g., `calculateSum`, `numItems`, `GraphBuilder`)
   - Coding styles:
     - brace style (inline, Allman, K&R)
     - indentation (2 vs 4 spaces)
   - Java features:
     - Generics, Enums, Interfaces, Inheritance, Lambdas
     - Java 8+ features (streams, Optionals, try-with-resources)
     - Single-class or multi-method format
"""

schema_sample = """```json
{
  "code": "public class Example { ... }",
  "feedback": {
    "Quality_MagicNumbers": [
      { "line": 3, "feedback": "Avoid magic numbers." }
    ],
    "OOP_LowCohesion": [
      { "line": 1, "feedback": "Class contains too many unrelated methods." }
    ]
  }
}
```"""

metrics = """Correctness_SyntaxError
Correctness_UndefinedVariable
Correctness_TypeMismatch
Correctness_LogicBug
Correctness_UnreachableCode
Correctness_IncorrectReturnType
Correctness_NullDereference
Correctness_IncorrectLoopBounds
Correctness_VariableShadowing
Correctness_IntegerOverflow
Correctness_ThreadSafety
Correctness_NonDeterminism
Quality_MagicNumbers
Quality_DeadCode
Quality_UnusedVariable
Quality_MethodLength
Quality_LineLength
Quality_RedundantOperations
Quality_UnnecessaryObjectCreation
Quality_InefficientDataStructure
Quality_BoxingUnboxing
Quality_StringConcatenationInLoop
Quality_CodeDuplication
Quality_CommentsQuality
Quality_JavadocMissing
Quality_OrderingInClass
Quality_NamingConventions
Quality_PoorSpacing
Quality_Indentation
Quality_StaticMethodOveruse
Quality_SingletonMisuse
Quality_AntiPatternDetected
OOP_SingleResponsibility
OOP_OpenClosedPrinciple
OOP_LiskovViolation
OOP_InterfaceSegregation
OOP_CompositionPreferred
OOP_InheritanceOveruse
OOP_AbstractionLeak
OOP_OverriddenEqualsHashcode
OOP_Encapsulation
OOP_PolymorphismMissing
OOP_TightCoupling
OOP_LowCohesion
OOP_CircularDependency
OOP_MissingFactoryPattern
OOP_ControllerLogicLeak
Security_HardcodedCredentials
Security_SensitiveLogging
Security_ExceptionSwallowing
Security_ExceptionHandling
Security_InjectionRisk
Security_MemoryLeakRisk
Security_ResourceManagement
Security_NonFinalStatic
Testability_NoTestsDetected
Testability_HardToMock
Testability_NoDependencyInjection
Performance_InefficientDataStructure
Performance_RedundantOperations
Performance_BoxingUnboxing
Performance_StringConcatenationInLoop
Performance_MemoryLeakRisk
Performance_LoopToStream"""

class PromptContext():
    def __init__(self):
        pass

    def domains(self):
        return prompt_domain

    def formatting_rules(self):
        return formatting_rules

    def schema_sample(self):
        return schema_sample

    def metrics(self):
        return metrics

    def build_prompt(self, n_issues: int):
        return f"""You are a **Java static code analyzer and code generator**.

Your task is to generate a *synthetic Java snippet* containing **exactly {n_issues} code issues**, with **high entropy**, drawn randomly from the metric list below.

# ✍️ Requirements

1. Generate realistic code that could be from:

{self.domains()}

{self.formatting_rules()}

3. For each injected issue, add structured feedback in this exact format:

{self.schema_sample()}

📌 Output format:

- Only a **single valid JSON object**.
- Code must be wrapped as a string under `"code"`, and contain correct Java syntax.
- `"feedback"` must **only include issues actually present** in the code.
- Each metric’s value is a list of {{ "line": <int>, "feedback": <string> }} objects.
- No extra comments or output beyond the JSON object.

🧠 Simulation Tips:

- Code should feel like it was written by:
  - 🐣 Beginner (redundant logic, logic bugs, bad naming)
  - 🧑‍💻 Intermediate (overly long methods, poor OOP)
  - 🧙 Advanced (concurrency bugs, misuse of patterns, tight coupling)

- Mix code lengths:
  - Short (~5 lines)
  - Long (20–30 lines)

- Include helper methods, nested classes, bad cohesion/single responsibility, or overloaded methods if useful.

--- Available Metrics (choose randomly) ---

{self.metrics()}

Now, generate a Java snippet with exactly {n_issues} injected issues and provide the structured feedback in JSON as described above.
"""