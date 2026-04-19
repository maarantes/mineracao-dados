-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: localhost    Database: db_gestao_ti
-- ------------------------------------------------------
-- Server version	8.0.45

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `chamados`
--

DROP TABLE IF EXISTS `chamados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chamados` (
  `id_chamado` int NOT NULL,
  `id_usuario` int DEFAULT NULL,
  `id_servico` int DEFAULT NULL,
  `data_abertura` date NOT NULL,
  `horas_trabalhadas` decimal(5,2) NOT NULL,
  PRIMARY KEY (`id_chamado`),
  KEY `fk_usuario` (`id_usuario`),
  KEY `fk_servico` (`id_servico`),
  CONSTRAINT `fk_servico` FOREIGN KEY (`id_servico`) REFERENCES `servicos` (`id_servico`),
  CONSTRAINT `fk_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chamados`
--

LOCK TABLES `chamados` WRITE;
/*!40000 ALTER TABLE `chamados` DISABLE KEYS */;
INSERT INTO `chamados` VALUES (1001,1,105,'2026-03-01',2.50),(1002,3,101,'2026-03-02',1.00),(1003,5,104,'2026-03-03',3.00),(1004,2,103,'2026-03-05',0.50),(1005,4,102,'2026-03-07',2.00),(1006,9,107,'2026-03-08',4.00),(1007,10,106,'2026-03-09',1.50),(1008,11,108,'2026-03-10',2.00),(1009,12,110,'2026-03-11',3.00),(1010,6,109,'2026-03-12',1.00),(1011,2,105,'2026-03-12',4.50),(1012,8,104,'2026-03-13',2.00),(1013,1,110,'2026-03-14',2.50),(1014,7,101,'2026-03-15',1.00),(1015,3,103,'2026-03-16',0.50),(1016,5,107,'2026-03-17',3.50),(1017,11,105,'2026-03-18',2.00),(1018,12,104,'2026-03-19',1.50),(1019,9,109,'2026-03-20',1.00),(1020,4,106,'2026-03-21',2.00);
/*!40000 ALTER TABLE `chamados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicos`
--

DROP TABLE IF EXISTS `servicos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servicos` (
  `id_servico` int NOT NULL,
  `nome_servico` varchar(100) NOT NULL,
  `categoria_servico` varchar(50) NOT NULL,
  `custo_hora` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id_servico`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicos`
--

LOCK TABLES `servicos` WRITE;
/*!40000 ALTER TABLE `servicos` DISABLE KEYS */;
INSERT INTO `servicos` VALUES (101,'Formatação Windows','S.O.',50.00),(102,'Instalação Linux','S.O.',70.00),(103,'Recuperação de Senha','Segurança',20.00),(104,'Configuração de Roteador','Redes',80.00),(105,'Erro no ERP','Aplicativo',100.00),(106,'Backup de Dados','Segurança',60.00),(107,'Manutenção de Hardware','Hardware',90.00),(108,'Treinamento de Software','Capacitação',120.00),(109,'Acesso VPN','Redes',75.00),(110,'Limpeza de Vírus','Segurança',85.00);
/*!40000 ALTER TABLE `servicos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id_usuario` int NOT NULL,
  `nome_usuario` varchar(100) NOT NULL,
  `departamento` varchar(50) NOT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Alice','RH'),(2,'Bruno','Financeiro'),(3,'Carlos','Vendas'),(4,'Daniela','Diretoria'),(5,'Eduardo','Vendas'),(6,'Fernanda','Marketing'),(7,'Gabriel','RH'),(8,'Helena','Financeiro'),(9,'Igor','TI'),(10,'Ariana','Marketing'),(11,'Kevin','Logística'),(12,'Larissa','Financeiro');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-03-03 22:22:52
