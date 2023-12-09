-- MySQL dump 10.13  Distrib 8.1.0, for macos13 (arm64)
--
-- Host: localhost    Database: DB_Final
-- ------------------------------------------------------
-- Server version	8.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `items`
--

DROP TABLE IF EXISTS `items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `items` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `stock` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=144 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `items`
--

LOCK TABLES `items` WRITE;
/*!40000 ALTER TABLE `items` DISABLE KEYS */;
INSERT INTO `items` VALUES (1,'XtraVision Headlight and Fog Light Bulb H11XV-2',25.66,10),(2,'Duralast Platinum AGM Battery H6-AGM Group Size 48 760 CCA',249.99,10),(3,'Spectra premium oil pan',142.99,10),(4,'AcDelco rear inner wheel bearing',211.99,10),(5,'Nutech long block engine',7196.99,10),(6,'Energy suspensino red end link grommet',15.99,10),(7,'Duralast gold ceramic brake pads',63.99,10),(8,'Duralast ceramic brake pads',45.99,10),(9,'Oil filter',12.99,10),(10,'delphi mass air flow sensor',405.99,10),(11,'Yukon gear axle unit',157.99,10),(12,'Duralast brake rotor pads',81.99,10),(13,'Duralast starter button',13.99,10),(14,'Ignition coil',13.39,10),(15,'Edlebrock clockwise rotation sensor',53.99,10),(16,'Edlebrock performance camshaft kit',252.99,10),(17,'Enviroshield cabin air filter',22.99,10),(18,'Dorman oil catch can',79.99,10),(19,'STP oil filter',9.99,10),(20,'Dorman fuel cap tether',1.79,10),(21,'STP cabin air filter',19.99,10),(22,'Proform transmission dipstick',37.99,10),(23,'Duralast locking fuel cap',11.99,10),(24,'Powerstop performance rotors',185.99,10),(25,'Fan blade motor',201.99,10),(26,'Lucas fuel treatment',6.99,10),(27,'Delphi fuel pump',988.99,10),(28,'Stoprite front brake pads',27.99,10),(29,'Duralast Gold Ceramic Brake Pads DG1363',56.99,10),(30,'Auto transaxle filter',51.59,10),(31,'Bypass hose',14.99,10),(32,'Remote oil filter mounting kit',80.39,10),(33,'Auto trans oil cooler',80.39,10),(34,'Control arm with ball joint',208.49,10),(35,'STP air filter',19.99,10),(36,'Trugrade steering pump',167.99,10),(37,'Adaptive front ceramic pads',81.99,10),(38,'TCI auto transmission filter OE',31.49,10),(39,'maxpower 3/32in premium fuel line',5.99,10),(40,'Schrader programmable OE TMPS',45.99,10),(41,'Air filter',22.99,10),(42,'Duralast ceramic brake pads',45.49,10),(43,'Duralast brake pads',38.99,10),(44,'TCI auto transmission filter',27.99,10),(45,'Air filter',27.99,10),(46,'Hopkins electrical wire connector',25.99,10),(47,'Holley EFI throttle position sensor',85.99,10),(48,'Anti lock right front sensor',194.99,10),(49,'Engine remanu',4880.00,10),(50,'Dorman OE solutions fuel line kit',22.49,10),(51,'Brake shoe repair kit',18.59,10),(52,'Brake rotor and pad kit',169.99,10),(53,'Trailer brake harness',30.99,10),(54,'Energy suspension black end link grommet set',14.99,10),(55,'Energy suspension red sway bar end links',22.99,10),(56,'Trans control solenoid',378.19,10),(57,'Duralast Brake Rotor 72006',96.99,10),(58,'National Powertrain Remanufactured Automatic Transmission Assembly T281605',2749.99,10),(59,'NuTech Remanufactured Automatic Transmission Assembly 8569A-74',2749.99,10),(60,'NuTech Remanufactured Long Block Engine DCVW',3739.99,10),(61,'STP Air Filter SA10110',24.99,10),(62,'STP Premium Air Filter PSA10110',24.99,10),(63,'Duralast Brake Pads D883',38.99,10),(64,'Duralast Semi-Metallic Brake Pads MKD1169A',40.00,10),(65,'NuTech Remanufactured Long Block Engine DCVX',4738.99,10),(66,'Duralast Radiator B13007',294.99,10),(67,'XtraVision Headlight and Fog Light Bulb H13XV-2',37.99,10),(68,'ACDelco Air Filter A3137C',26.99,10),(69,'XtraVision Headlight and Fog Light Bulb H11XV-2',37.99,10),(70,'Camshaft sensor',11.99,10),(71,'Dahmer Powertrain Longblock Engine L5310GMCCI',4125.99,10),(72,'Duralast Battery T5-DL Group Size T5 590 CCA',189.99,10),(73,'COMP cam performance cam',182.99,10),(74,'Moveras Remanufactured Automatic Transmission Assembly M02135',2587.99,10),(75,'Duralast Platinum EFB Battery H6-EFB Group Size 48 750 CCA',239.99,10),(76,'Duralast Brake Pads D1194',45.49,10),(77,'National Powertrain Remanufactured Automatic Transmission Assembly T282004',2884.99,10),(78,'Mobil 1 fuel eco 0w20',46.49,10),(79,'STP Air Filter SA10690',19.99,10),(80,'Duralast Brake Pads MKD1337',44.99,10),(81,'Duralast Platinum AGM Battery H7-AGM Group Size 94R 850 CCA',249.99,10),(82,'AC delco oil filter',10.49,10),(83,'Duralast Semi-Metallic Brake Pads MKD1404',44.49,10),(84,'K&N oil filter',17.49,10),(85,'Duralast electrical wire connector',59.99,10),(86,'All Trans Remanufactured Automatic Transmission Assembly A204003',2643.99,10),(87,'Duralast Ceramic Brake Pads MKD1033',24.99,10),(88,'STP Cabin Air Filter CAF9957P',19.99,10),(89,'Dahmer Powertrain Long Block Engine 253546',4437.99,10),(90,'TruGrade Fuel Pump D6632M',259.99,10),(91,'Fuel injector',319.39,10),(92,'STP Extended Life Oil Filter S10060XL',38.99,10),(93,'STP Extended Life Oil Filter S10060XL',9.99,10),(94,'Knock sensor',12.99,10),(95,'Trans control solenoid',226.59,10),(96,'Front upper left control arm',571.79,10),(97,'Dahmer Powertrain Longblock Engine L5310GMCCJ',4125.99,10),(98,'Dahmer Powertrain Long Block Engine 253545',4437.99,10),(99,'Power steering filter',25.99,10),(100,'Rack and pinion',529.99,10),(101,'Delphi Fuel Pump CFG1055',359.99,10),(102,'STP Extended Life Oil Filter S9018RXL',10.99,10),(103,'TruGrade Fuel Pump D6631M',259.99,10),(104,'STP Air Filter SA9492',17.99,10),(105,'Duralast front drvr brake caliper',103.99,10),(106,'Duralast front pass brake caliper',103.99,10),(107,'Steering knuckle front right',367.99,10),(108,'Steering knuckle front left',367.99,10),(109,'STP Premium Air Filter PSA9492',24.99,10),(110,'Spectre 27in transmission dipstick',23.99,10),(111,'Cooling temp sensor',55.79,10),(112,'Duralast relay',14.99,10),(113,'All Trans Remanufactured Automatic Transmission Assembly A173057',1955.99,10),(114,'Duralast ceramic brake rotor',69.99,10),(115,'Dorman engine coolant temp sensor clip',10.29,10),(116,'STP oil filter',11.49,10),(117,'Duralast power steering pump',248.99,10),(118,'All Trans Remanufactured Automatic Transmission Assembly A173056',1955.99,10),(119,'Durlast Bearing',166.99,10),(120,'Compressor works power steering cooler line',27.99,10),(121,'STP Oil Filter S9018R',11.99,10),(122,'Duralast Gold Battery T5-DLG Group Size 90 650 CCA',209.99,10),(123,'Compressor works trans oil cooler',66.99,10),(124,'Duralast auto trans filter',27.99,10),(125,'Auto trans cooler kit',23.79,10),(126,'Premium air filter',26.99,10),(127,'K&N high perf air intake system',449.99,10),(128,'Starter',129.79,10),(129,'Auto trans filter kit',26.79,10),(130,'Dorman brake ABS sensor',41.99,10),(131,'Intake valve stem seal',4.59,10),(132,'Dorman coolant temp sensor',33.99,10),(133,'Standard LED 194 mini',9.99,10),(134,'Engine remanu',6070.00,10),(135,'Silentguard rear brake pads',49.99,10),(136,'Air temp sensor',109.19,10),(137,'Ball joint front lower',39.19,10),(138,'Gold cabin filter',72.99,10),(139,'Throttle body unit',15.99,10),(140,'Air helper spring kit',114.99,10),(141,'Brake hose',28.99,10),(142,'Headlight connector',14.59,10),(143,'Ball joint front lower',39.19,10);
/*!40000 ALTER TABLE `items` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-09  2:00:06
