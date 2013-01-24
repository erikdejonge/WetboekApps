//
//  BestuursrechtAppDelegate.m
//  Bestuursrecht
//
//  Created by rabshakeh on 10/14/09 - 12:09 PM.
//  Copyright __MyCompanyName__ 2011. All rights reserved.
//

#import "BestuursrechtAppDelegate.h"
#import "BestuursrechtViewController.h"
#import "TableViewFromDatabaseViewController.h"
#import "ArtikelViewControllerFromXIB.h"
#import "WetboekSearchViewController.h"

@implementation BestuursrechtAppDelegate

@synthesize window ;
@synthesize viewController ;


-(void) applicationDidFinishLaunching: (UIApplication *) application
{
  TableViewFromDatabaseViewController *tableViewFromDatabaseController = [[TableViewFromDatabaseViewController alloc] init] ;

  tableViewFromDatabaseController.table_name = @"wetboekhoofdstuk" ;
  tableViewFromDatabaseController.next_table = @"wetboek" ;
  tableViewFromDatabaseController.title      = @"Bestuursrecht - Apr.2011" ;
  [tableViewFromDatabaseController reload] ;
  navigationController = [[UINavigationController alloc] initWithRootViewController:tableViewFromDatabaseController] ;

  [tableViewFromDatabaseController release] ;
  navigationController.navigationBar.tintColor = [UIColor colorWithRed:0.066666666666666666 green:0.24313725490196078 blue:0.36470588235294116 alpha:0] ;

  [window addSubview:[navigationController view]] ;

  [window makeKeyAndVisible] ;
}


-(void) dealloc
{
  [navigationController release] ;
  [viewController release] ;
  [window release] ;
  [super dealloc] ;
}


@end
