-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: localhost    Database: db_locadora
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
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `id_cliente` int NOT NULL,
  `nome` varchar(100) NOT NULL,
  `cidade` varchar(50) NOT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_cliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (1,'Carlos Silva','São Paulo','11999990001'),(2,'Ana Souza','Campinas','11999990002'),(3,'Bruno Lima','Santos','11999990003'),(4,'Fernanda Alves','São Paulo','11999990004'),(5,'Juliana Rocha','Osasco','11999990005'),(6,'Ricardo Mendes','Guarulhos','11999990006'),(7,'Mariana Costa','Sorocaba','11999990007'),(8,'Lucas Martins','São Bernardo','11999990008'),(9,'Patricia Gomes','São Paulo','11999990009'),(10,'Eduardo Nunes','Campinas','11999990010'),(11,'Gabriel Ferreira','Barueri','11999990011'),(12,'Amanda Ribeiro','São Paulo','11999990012'),(13,'Thiago Santos','Campinas','11999990013'),(14,'Beatriz Lima','Santos','11999990014'),(15,'Rafael Costa','Osasco','11999990015');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locacoes`
--

DROP TABLE IF EXISTS `locacoes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `locacoes` (
  `id_locacao` int NOT NULL,
  `id_cliente` int DEFAULT NULL,
  `id_veiculo` int DEFAULT NULL,
  `data_inicio` date NOT NULL,
  `data_fim` date NOT NULL,
  `dias_alugados` int NOT NULL,
  `valor_total` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id_locacao`),
  KEY `id_cliente` (`id_cliente`),
  KEY `id_veiculo` (`id_veiculo`),
  CONSTRAINT `locacoes_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`),
  CONSTRAINT `locacoes_ibfk_2` FOREIGN KEY (`id_veiculo`) REFERENCES `veiculos` (`id_veiculo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locacoes`
--

LOCK TABLES `locacoes` WRITE;
/*!40000 ALTER TABLE `locacoes` DISABLE KEYS */;
INSERT INTO `locacoes` VALUES (1001,1,101,'2026-03-01','2026-03-03',2,240.00),(1002,2,105,'2026-03-02','2026-03-05',3,1050.00),(1003,3,103,'2026-03-04','2026-03-06',2,440.00),(1004,4,108,'2026-03-05','2026-03-07',2,1200.00),(1005,5,102,'2026-03-06','2026-03-08',2,230.00),(1006,6,107,'2026-03-07','2026-03-10',3,1350.00),(1007,7,106,'2026-03-08','2026-03-11',3,990.00),(1008,8,104,'2026-03-09','2026-03-12',3,630.00),(1009,9,101,'2026-03-10','2026-03-12',2,240.00),(1010,10,105,'2026-03-11','2026-03-14',3,1050.00),(1011,1,103,'2026-03-12','2026-03-15',3,660.00),(1012,2,106,'2026-03-13','2026-03-16',3,990.00),(1013,3,108,'2026-03-14','2026-03-16',2,1200.00),(1014,4,102,'2026-03-15','2026-03-18',3,345.00),(1015,5,101,'2026-03-16','2026-03-18',2,240.00),(1016,6,105,'2026-03-17','2026-03-20',3,1050.00),(1017,7,107,'2026-03-18','2026-03-21',3,1350.00),(1018,8,109,'2026-03-19','2026-03-22',3,960.00),(1019,9,111,'2026-03-20','2026-03-22',2,200.00),(1020,10,113,'2026-03-21','2026-03-24',3,1950.00),(1021,11,109,'2026-03-19','2026-03-22',3,960.00),(1022,12,111,'2026-03-20','2026-03-23',3,300.00),(1023,13,113,'2026-03-21','2026-03-24',3,1950.00),(1024,14,114,'2026-03-22','2026-03-25',3,2100.00),(1025,15,110,'2026-03-23','2026-03-26',3,1020.00),(1026,11,115,'2026-03-24','2026-03-27',3,1440.00),(1027,12,112,'2026-03-25','2026-03-27',2,220.00),(1028,13,109,'2026-03-26','2026-03-29',3,960.00),(1029,14,111,'2026-03-27','2026-03-29',2,200.00),(1030,15,113,'2026-03-28','2026-03-31',3,1950.00);
/*!40000 ALTER TABLE `locacoes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `veiculos`
--

DROP TABLE IF EXISTS `veiculos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `veiculos` (
  `id_veiculo` int NOT NULL,
  `modelo` varchar(100) NOT NULL,
  `categoria` varchar(50) NOT NULL,
  `valor_diaria` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id_veiculo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `veiculos`
--

LOCK TABLES `veiculos` WRITE;
/*!40000 ALTER TABLE `veiculos` DISABLE KEYS */;
INSERT INTO `veiculos` VALUES (101,'Onix','Econômico',120.00),(102,'HB20','Econômico',115.00),(103,'Corolla','Sedan',220.00),(104,'Civic','Sedan',210.00),(105,'Compass','SUV',350.00),(106,'HR-V','SUV',330.00),(107,'Hilux','Utilitário',450.00),(108,'BMW 320i','Luxo',600.00),(109,'Tracker','SUV',320.00),(110,'Renegade','SUV',340.00),(111,'Fiat Mobi','Econômico',100.00),(112,'Gol','Econômico',110.00),(113,'Audi A4','Luxo',650.00),(114,'Mercedes C180','Luxo',700.00),(115,'Ranger','Utilitário',480.00);
/*!40000 ALTER TABLE `veiculos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-03-03 22:36:46
